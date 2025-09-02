from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, make_response
)
from werkzeug.exceptions import abort

from flaskapp.authjson import login_required

from typing import List

import requests
import os

def put_into_database(dict_arg: dict, endpoint: str):
    response = requests.put(endpoint, json=dict_arg)
    if not response:
        abort(404, 'Evaluation failed.')
    pass

#################### Evaluate Python, may implement later
judge_results : List[str] = []

def append_judge_results(assessment_result: List[str] | str) -> None:
    """
    An importable method for judge.py.

    Appends to judge_results (global variable) a string of judge results, based on a string or
    a list of strings.

    Parameters:
        assessment_result: If the value passed is a list of strings, then a string connecting
            the elements of this list will be appended to judge_results. If it is a string, it
            will be appended directly to judge_results.
    """
    assert isinstance(assessment_result, str) or isinstance(assessment_result, list), \
        'assessment_result is not a string nor a list'
    if isinstance(assessment_result, list):
        assert all(isinstance(element, str) for element in assessment_result), \
            'There is a non-string element in assessment_result'
        judge_results.append('\n'.join(assessment_result))
    else:
        judge_results.append(assessment_result)

def get_average_overall_score() -> float:
    """
    Gets the average overall score from judge_results (rounded to 2 decimal digits),
    once it no longer gets appended when necessary.

    Returns:
        the average overall score from judge_results (rounded to 2 decimal digits)
    """
    # The final sentence of each item in judge_results contains the score for its corresponding question (at least for now).
    # It follows the syntax: "SCORE FOR THIS QUESTION: <score>%".
    # Therefore to extract the score from this, slice with start_index = str.find(': ') + 2, end_index = str.find('%')
    # Round the float(score) to 2 decimal digits (as used in judge.py).
    # Take the sum of all these scores and divide it by len(judge_results) to get the average score

    score_sum: float = 0.0

    for result in judge_results:
        # Extract the final sentence of result
        score_sentence: str = result[result.rfind('\n') + 1 : ]
        score_str = score_sentence[score_sentence.find(': ') + 2 : score_sentence.find('%')]
        score = round(float(score_str), 2)
        score_sum += score

    return round(score_sum / len(judge_results), 2)

def commit_judge_results(id: str) -> None:
    """
    Commit judge_results into the database

    Parameters:
        id (str): The user's ID
    """
    assert isinstance(id, str), 'id is not a string'
    pre_commit_entry = requests.get(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{id}').json()
    if pre_commit_entry and isinstance(pre_commit_entry, dict):
        post_commit_entry = pre_commit_entry
        post_commit_entry['evaluation'] = judge_results
        post_commit_entry['final-average-score'] = str(get_average_overall_score())

        import requests
        submit_response = requests.put(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{id}', json=post_commit_entry)
        if submit_response.status_code == 200:
            print(f'Successfully submitted the evaluation for {id}!')
        else:
            print(f'Unsuccessfully submitted the evaluation for {id}.')
        return
    print(f'Unable to read and evaluate {id}\'s answers!')
    pass

def launch_evaluation(id: str, answer_list: List[str]) -> None:
    """
    Launches the process of evaluating the list of the users' answers.

    Parameters:
        id (str): The user's ID
        answer_list (str): A list of answers, all of which are string values
    """
    assert isinstance(answer_list, list), 'answer_list is not a list'

    # Reset/clear judge_results
    judge_results.clear()

    # In each 'examination_<number>' folder in 'examinations' folder, create a response.py and paste the respective code from answer_list

    for i in range(0, len(answer_list), 1):
        assert isinstance(answer_list, str), 'There is a non-string element in answer_list'
        try:
            with open(f'examinations/examination_{i}/response.py', 'w') as file:
                file.write(answer_list[i])
        except FileNotFoundError as e: # If the parent directory does not exist
            print('<FileNotFoundError> examination_{i} failed: {e}')
            return

    # Run init.py in 'examinations'
    try:
        from examinations.__init__ import run_judge
    except ModuleNotFoundError as e:
        print('<ModuleNotFoundError> Importing examinations.__init__ failed: {e}')
    except ImportError as e:
        print('<ImportError> There is an issue with importing run_judge from examinations.__init__: {e}')
    else:
        for i in range(0, len(answer_list), 1):
            try:
                run_judge(f'flask\\flaskapp\\examinations\\examination_{i}')
            except Exception as e:
                print(f'<Error> judge.py is missing or unreadable in examination_{i}: {e}')
            pass

        # Display the judge results on the client side
        commit_judge_results(id)
    pass
################# Implement later ######################
    

bp = Blueprint('eval', __name__, url_prefix='/eval')

@bp.route('/submit/<id>', methods=['PUT'])
@login_required
def submit(id: str):
    if request.method == 'PUT':
        answers : dict = request.json
        url = f'{os.getenv('ANSWERS_ENDPOINT')}/{id}'
        put_into_database(answers, url)
        launch_evaluation(list(answers.values))
    return redirect(url_for('index'))
    

@bp.route('/view/<id>', methods=['GET'])
@login_required
def determine_viewability(id: str) -> dict:
    '''
    Returns a dictionary of 2 entries indicating if the code should be viewable or not
    '''
    if request.method == 'GET':
        # Send a GET request for the JSON of the user's code stored in the database
        user_info = requests.get(f'{os.getenv('ANSWERS_ENDPOINT')/{id}}')

        user_info_json = user_info.json
        
        response_body = {
            'answers_viewable': False, # Indicates if the user's submission is to be displayed (uneditable)
            'evaluation_viewable': False # Indicates if the evaluation of the user's submission is to be displayed
        }

        if user_info_json['answers'] and len(user_info_json['answers']) > 0:
            # If the user has submitted their answer already
            response_body['answers_viewable'] = True
        
        response = make_response(response_body, 200)
        response.headers['Content-Type'] = 'text/plain'
        return response
    return redirect(url_for('index')) # Simply redirect back to APP


