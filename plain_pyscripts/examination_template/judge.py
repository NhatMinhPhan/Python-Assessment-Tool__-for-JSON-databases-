from typing import Union, List

# In each 'examination' folder, there are only 2 files: judge.py & response.py.
# Find respective 'response.py' in this 'examination' folder

import_failed = True

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
        elif isinstance(test_case_result, bool) and test_case_result == True: # Passed
            print(f"{func.__name__} passed.")
        else:
            raise ValueError('This test case function return either a single boolean False, or a value that is not a string nor boolean.')
        return test_case_result
    return wrapper

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
    else:
        fails = results.count(False) # when test_case() != True
        fail_percentage = round(fails/len(results)*100, 2)
        print(f'Failed {fails}/{len(results)} cases ({fail_percentage}%).\n_______________________________________')
    return test_ok

@test_case
def test_case_1() -> Union[bool, str]:
    """
    Test case.

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
    run()