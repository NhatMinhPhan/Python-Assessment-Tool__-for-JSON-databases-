from typing import Union, List

# In each 'examination' folder, there are only 2 files: judge.py & response.py.
# Find respective 'response.py' in this 'examination' folder

import_failed = True

displayable_results: List[str] = [] # Results displayable to the user if they are set as viewable

# @after_successful_import decorator
def after_successful_import(func):
    """
    Functions with this decorator can only run after successfully importing response.py.
    """
    def wrapper(*args, **kwargs):
        if import_failed:
            print('Unable to proceed due to failed import of response.py')
            return
        return func(*args, **kwargs)
    return wrapper

# @test_case decorator
def test_case(func):
    """
    This decorator indicates that the function which it modifies is a test case.
    All test case functions must return either a boolean or a string value.
    """
    def wrapper(*args, **kwargs):
        test_case_result = func(*args, **kwargs)
        if isinstance(test_case_result, str): # Failed
            print(f"{func.__name__} failed: {test_case_result}.")
            displayable_results.append(f"{func.__name__} failed: {test_case_result}.")
        elif isinstance(test_case_result, bool) and test_case_result == True: # Passed
            print(f"{func.__name__} passed.")
            displayable_results.append(f"{func.__name__} passed.")
        else:
            # Clear displayable_results and display an error message
            displayable_results.clear()
            displayable_results.append("ERROR! Please contact your tutor/administrator for support.")

            raise ValueError('This test case function return either a single boolean False, or a value that is not a string nor boolean.')
        return test_case_result
    return wrapper

def get_user_id() -> str:
    """
    Retrieves the user ID from the first line of response.py.

    Returns:
        A user ID string
    """
    with open('response.py', 'r') as file:
        first_line = file.readline().strip()
        # Remove the '# ID: '
        return first_line[6:]

@after_successful_import
def run() -> bool:
    """
    Invoke the judge (as in judge.py) and examine response.py.

    Returns:
        True if response.py satisfies the requirements set out by this instance of judge.py
        False otherwise
    """
    results: List[bool] = []

    # Since test case functions return either a bool or a str,
    # append boolean values corresponding to if they return True to results
    results.append(test_case_1() == True)
    # results.append(test_case_2() == True)
    # results.append(test_case_3() == True)
    
    test_ok: bool = False not in results
    if test_ok:
        print('TEST OK\n_______________________________________')
        displayable_results.append('TEST OK\n_______________________________________')

        # Append a score of 100% to displayable_results
        displayable_results.append('SCORE FOR THIS QUESTION: 100%')
    else:
        fails = results.count(False) # when test_case() != True
        fail_percentage = round(fails/len(results)*100, 2)
        print(f'Failed {fails}/{len(results)} cases ({fail_percentage}%).\n_______________________________________')
        displayable_results.append(f'Failed {fails}/{len(results)} cases ({fail_percentage}%).\n_______________________________________')

        # Determine the score and append it to displayable_results
        GRADE = 100 - fail_percentage
        displayable_results.append(f'SCORE FOR THIS QUESTION: {GRADE}%')
    
    # Regardless of the result, send the results to the database.

    import requests
    import os
    SENT_STRING : str = '\n'.join(displayable_results)
    USER_ID = get_user_id()
    ENDPOINT = f'{os.getenv('SUBMISSIONS_ENDPOINT')}{USER_ID}'
    user_submission = requests.get(ENDPOINT)
    assert user_submission.status_code == 200, 'Cannot fetch user_submission'
    new_submission = user_submission.json()
    new_submission['evaluation'].append(SENT_STRING)
    print(f'The new submission: {new_submission}')
    response = requests.put(ENDPOINT, json=new_submission)
    print(f'Sent to {ENDPOINT}: {response.status_code}\n{response}')
    
    return test_ok

@test_case
def test_case_output() -> Union[bool, str]:
    """
    Test case if response.py yields the correct output.

    Returns:
        A single boolean value if the test case passes.
        A string value if the test case fails.
        Boolean:
            True if the test case passes.
            False if the test case fails.
        String: error message if the test case fails.

    """
    # try:
    #   from response import func_or_class
    # except ImportError as e:
    #   return (f'Import Error: {e}')

    # example_var = 
    # expected = 

    # try:
    #    result = func_or_class(example_var)
    #except Exception as e:
    #    message = f'func_or_class({example_var}) expects a result, but got an exception: {str(e).capitalize()}'
    #    return message

    # if expected != result:
    #    message = f'func_or_class({example_var}) expects {expected}, but got {result}'
    #    return message
    #return True
    pass

@test_case
def test_case_exception() -> Union[bool, str]:
    """
    Test case if response.py raises an exception, either general or particular.

    Returns:
        A single boolean value if the test case passes.
        A string value if the test case fails.
        Boolean:
            True if the test case passes.
            False if the test case fails.
        String: error message if the test case fails.

    """
    # try:
    #   from response import func_or_class
    # except ImportError as e:
    #   return (f'Import Error: {e}')

    # Check if the code raises an exception

    # try:
    #    result = func_or_class(example_var)
    # except Exception as e:
    #    return True
    # else:
    #    message = f'func_or_class({example_var}) expects an exception, but didn\'t get one'
    #    return message
    pass

@test_case
def test_case_1() -> Union[bool, str]:
    """
    Test case if response.py yields the correct output.

    Returns:
        A single boolean value if the test case passes.
        A string value if the test case fails.
        Boolean:
            True if the test case passes.
            False if the test case fails.
        String: error message if the test case fails.

    """
    try:
      from response import double_the_int
    except ImportError as e:
      return (f'Import Error: {e}')

    argument = 6
    expected = 12

    try:
       result = double_the_int(argument)
    except Exception as e:
       message = f'double_the_int() expects a result, but got an exception: {str(e).capitalize()}'
       return message

    if expected != result:
       message = f'double_the_int() expects {expected}, but got {result}'
       return message
    return True
    pass

##########################################################

# Import response.py
try:
    import response
except SyntaxError as e:
    print('JUDGE: Invalid syntax found in response.py')

    # Get the name of e's type and eliminate "<class '" and "'>"
    type_name = str(type(e))
    type_name = type_name.replace('<class \'', '')
    type_name = type_name.replace('\'>', '')

    print(f'Details: <{type_name}> {e}')
except ModuleNotFoundError as e:
    print('JUDGE: response.py cannot be found')

    # Get the name of e's type and eliminate "<class '" and "'>"
    type_name = str(type(e))
    type_name = type_name.replace('<class \'', '')
    type_name = type_name.replace('\'>', '')

    print(f'Details: <{type_name}> {e}')
except Exception as e:
    print('JUDGE: There has been an exception while importing response.py')
    
    # Get the name of e's type and eliminate "<class '" and "'>"
    type_name = str(type(e))
    type_name = type_name.replace('<class \'', '')
    type_name = type_name.replace('\'>', '')

    print(f'Details: <{type_name}> {e}')
else:
    import_failed = False
    print("JUDGE: Successfully found corresponding response.py!")
    print('_______________________________________\nTEST CASES:')
    displayable_results.append('TEST CASES:')
    import sys
    sys.path.append('C:/Users/nhatm/programming projs/FlaskPythonAssessment/venv/Lib/site-packages')
    run()