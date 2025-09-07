from flask import (
    Blueprint, request, make_response, Response
)
from werkzeug.exceptions import abort

from flaskapp.authjson import login_required

from typing import List

from flask_cors import cross_origin

import requests
import os

import sys
sys.path.append('C:/Users/nhatm/programming projs/FlaskPythonAssessment/flask/flaskapp')
from authjson import cors_required_headers

def put_into_database(answer_list: list, endpoint: str):
    """ PUT 'answers' item into the database """
    answer_dict : dict = { 'answers' : answer_list, 'evaluation' : [] }
    response = requests.put(endpoint, json = answer_dict)
    if response.status_code != 200:
        abort(404, 'Evaluation failed.')
    pass

def censor_all_directories_in_list (list_arg: List[str]) -> List[str]:
    """
    Replaces all sensitive sections of all directories found in a list with an ellipsis (...).

    Parameters:
        list_arg (list[str]): A list of strings with potentially sensitive information

    Returns:
        A list of strings with all sensitive sections of all directories replaced with an ellipsis (...)
    """
    assert isinstance(list_arg, list), "list_arg is not a list"
    assert all(isinstance(item, str) for item in list_arg), "There is a non-string element in list_arg."
    import os
    return [item.replace(os.getenv('CENSORED_DIRECTORY_SECTION'), ' ... ') for item in list_arg]

def get_average_overall_score(id: str) -> float:
    """
    Gets and sends to the database the average overall score from judge_results
    (rounded to 2 decimal digits), once it no longer gets appended when necessary.

    Parameters:
        id (str): User ID

    Returns:
        the average overall score from judge_results (rounded to 2 decimal digits)
    """
    # The final sentence of each item in judge_results contains the score for its corresponding question (at least for now).
    # It follows the syntax: "SCORE FOR THIS QUESTION: <score>%".
    # Therefore to extract the score from this, slice with start_index = str.find(': ') + 2, end_index = str.find('%')
    # Round the float(score) to 2 decimal digits (as used in judge.py).
    # Take the sum of all these scores and divide it by len(judge_results) to get the average score
    score_sum: float = 0.0

    submission = requests.get(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{id}').json()
    print(f'Submission for ave overall score: {submission}')
    judge_results = submission['evaluation']

    assert judge_results, 'judge_results is None'

    for result in judge_results:
        # Extract the final sentence of result
        score_sentence: str = result[result.rfind('\n') + 1 : ]
        score_str = score_sentence[score_sentence.find(': ') + 2 : score_sentence.find('%')]
        score = round(float(score_str), 2)
        score_sum += score
    return round(score_sum / len(judge_results), 2)

def submit_average_overall_score(id: str) -> None:
    """
    Submits the pre-calculated average overall score.

    Parameters:
        id (str): User ID
    """
    overall_average = get_average_overall_score(id)
    user_submission = requests.get(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{id}').json()
    assert user_submission, 'user_submission is None'
    user_submission['overall-average'] = overall_average
    response = requests.put(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{id}', json = user_submission)
    if response.status_code != 200:
        abort(500, 'Evaluation failed.')

def launch_evaluation(id: str, answer_list: List[str]) -> None:
    """
    Launches the process of evaluating the list of the users' answers.

    Parameters:
        id (str): The user's ID
        answer_list (str): A list of answers, all of which are string values
    """
    assert isinstance(answer_list, list), 'answer_list is not a list'

    # In each 'examination_<number>' folder in 'examinations' folder, create a response.py and paste the respective code from answer_list

    for i in range(0, len(answer_list), 1):
        assert isinstance(answer_list[i], str), 'There is a non-string element in answer_list'
        try:
            with open(f'flask/flaskapp/examinations/examination_{i}/response.py', 'w') as file:
                file.write(f'# ID: {id}\n\n')
                file.write(answer_list[i])
        except FileNotFoundError as e: # If the parent directory does not exist
            print(f'<FileNotFoundError> examination_{i} failed: {e}')
            return

    # Run init.py in 'examinations'
    try:
        from examinations.judge_driver import run_judge
    except ModuleNotFoundError as e:
        print(f'<ModuleNotFoundError> Importing examinations.judge_driver failed: {e}')
    except ImportError as e:
        print(f'<ImportError> There is an issue with importing run_judge from examinations.judge_driver: {e}')
    else:
        for i in range(0, len(answer_list), 1):
            try:
                run_judge(f'flask\\flaskapp\\examinations\\examination_{i}')
            except Exception as e:
                print(f'<Error> judge.py is missing or unreadable in examination_{i}: {e}')
            pass

        submit_average_overall_score(id)
    pass
    
bp = Blueprint('eval', __name__, url_prefix='/eval')

@cross_origin # Enables CORS
@bp.route('/submit/<id>', methods=['PUT'])
# @login_required
def submit(id: str):
    if request.method == 'PUT':
        print(f"Putting {id}'s submission into the database...")
        answers : List = request.json['answers']
        print(f"{id}:\n{answers}")
        url = f'{os.getenv('SUBMISSIONS_ENDPOINT')}{id}'
        put_into_database(answers, url)
        print("Launching evaluation...")
        launch_evaluation(id = id, answer_list = answers)
        print("Completing evaluation...")
        return Response(status=200, headers=cors_required_headers, response='The submission has been processed successfully.')
    return Response(status=403, headers=cors_required_headers, response='Inaccessible.')
    
@cross_origin # Enables CORS
@bp.route('/view/<id>', methods=['GET'])
# @login_required
def determine_viewability(id: str):
    '''
    Returns a dictionary of 2 entries indicating if the code should be viewable or not.
    Unused for now.
    '''
    if request.method == 'GET':
        print(f'Determining viewability settings for {id}...')
        # GET admin-data from the JSON database
        # NOTE: admin_data will store a list because of the endpoint used, explaining why [0] is used (it only has 1 item).
        admin_data = requests.get(os.getenv('ADMINDATA_ENDPOINT')).json()[0]

        # GET the user's submission data from the JSON database
        user_info = requests.get(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{id}').json()

        if (not admin_data) or (not user_info):
            return Response(status=500, headers=[('Access-Control-Allow-Origin', '*')], response='Viewability undetermined')
        
        response_body = {
            # Indicates if the user has made a submission
            'submitted': True,

            # Indicates if the user's submission is to be displayed (uneditable)
            'answers_viewable': bool(admin_data['answers_viewable']),

            # Indicates if the evaluation of the user's submission is to be displayed
            'evaluation_viewable': bool(admin_data['evaluation_viewable'])
        }

        if ('answers' not in user_info) or len(user_info['answers']) <= 0:
            # If the user has not yet submitted their answers
            response_body['submitted'] = False
            response_body['answers_viewable'] = False
            response_body['evaluation_viewable'] = False
        
        print(f'Visibility settings for {id}:\n{response_body}')

        import json
        response_body_json = json.dumps(response_body) # Converts dict to JSON
        
        return Response(status=200, headers=cors_required_headers, response=response_body_json, content_type='application/json')
    return Response(status=403, headers=cors_required_headers, response='Inaccessible')

@cross_origin # Enables CORS
@bp.route('/results/<id>', methods=['GET'])
def get_evaluation_results(id: str):
    if request.method == 'GET':
        submission_json = requests.get(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{id}').json()
        if not submission_json:
            return Response(status=500, headers=cors_required_headers, response='Inaccessible')
        if 'evaluation' not in submission_json:
            return Response(status=404, headers=cors_required_headers, response='\'evaluation\' not found.')
        if 'overall-average' not in submission_json:
            return Response(status=404, headers=cors_required_headers, response='\'overall-average\' not found.')
        evaluation_text = submission_json['evaluation']
        overall_average = submission_json['overall-average']
        
        # The last item in evaluation_text or 'evaluation' in the JSON is the overall average score.
        evaluation_text.append(f'Your overall average score is: {overall_average}%')
        evaluation_text = censor_all_directories_in_list(evaluation_text)
        response_body = {
            'evaluation': evaluation_text
        }
        
        print(f'Evaluation_text: {evaluation_text}', type(evaluation_text))
        import json
        response_body_json = json.dumps(response_body)
        return Response(status=200, headers=cors_required_headers, response=response_body_json, content_type='application/json')
    return Response(status=403, headers=cors_required_headers, response='Inaccessible')

@cross_origin
@bp.route('/user-code/<id>', methods=['GET'])
def view_user_code(id: str):
    if request.method == 'GET':
        submission_json = requests.get(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{id}').json()
        if not submission_json:
            return Response(status=500, headers=cors_required_headers, response='Inaccessible')
        if 'answers' not in submission_json:
            return Response(status=404, headers=cors_required_headers, response='\'answers\' not found.')
        submission = submission_json['answers']
        response_body = {
            'submission': submission
        }
        import json
        response_body_json = json.dumps(response_body)
        return Response(status=200, headers=cors_required_headers, response=response_body_json, content_type='application/json')
    return Response(status=403, headers=cors_required_headers, response='Inaccessible')


