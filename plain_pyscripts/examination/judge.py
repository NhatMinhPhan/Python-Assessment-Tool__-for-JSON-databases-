from typing import Union, List

# In each 'examination' folder, there are only 2 files: judge.py & response.py.
# Find respective 'response.py' in this 'examination' folder

import_failed = True

# @after_successful_import decorator
def after_successful_import(func):
    def wrapper(*args, **kwargs):
        if import_failed:
            print('Unable to proceed due to failed import of response.py')
            return
        return func(*args, **kwargs)
    return wrapper

# @test_case decorator
def test_case(func): # All test case functions must return either a bool or a str
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
    # Add custom code for response.py here

    # Since test case functions return either a bool or a str,
    # append boolean values corresponding to if they return True to results
    results.append(test_case_1() == True)
    results.append(test_case_2() == True)
    results.append(test_case_3() == True)
    results.append(test_case_4() == True)
    results.append(test_case_5() == True)
    
    test_ok: bool = False not in results
    if test_ok:
        print('TEST OK\n_______________________________________')
    else:
        fails = results.count(False) # when test_case() != True
        print(f'Failed {fails}/{len(results)} cases.\n_______________________________________')
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
    from response import add_ints

    expected = 5
    try:
        result = add_ints(2, 3)
    except Exception as e:
        message = f'add_ints(2, 3) expects a result, but got an exception: {e.capitalize()}'
        return message

    if expected != result:
        message = f'add_ints(2, 3) expects {expected}, but got {result}'
        return message
    return True

@test_case
def test_case_2() -> Union[bool, str]:
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
    from response import add_ints

    expected = -5
    try:
        result = add_ints(-5)
    except Exception as e:
        message = f'add_ints(-5) expects a result, but got an exception: {e.capitalize()}'
        return message
    
    if expected != result:
        message = f'add_ints(-5) expects {expected}, but got {result}'
        return message
    return True

@test_case
def test_case_3() -> Union[bool, str]:
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
    from response import add_ints

    expected = 100
    try:
        result = add_ints(100, 2, 8, -8, -2)
    except Exception as e:
        message = f'add_ints(100, 2, 8, -8, -2) expects a result, but got an exception: {e.capitalize()}'
        return message
    
    if expected != result:
        message = f'add_ints(100, 2, 8, -8, -2) expects {expected}, but got {result}'
        return message
    return True

# This test case examines if the code raises an exception
@test_case
def test_case_4() -> Union[bool, str]:
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
    # Check if the code raises an exception
    from response import add_ints

    try:
        result = add_ints(-2.5)
    except Exception as e:
        return True
    else:
        message = 'add_ints(-2.5) expects an exception, but didn\'t get one.'
        return message

# This test case examines if the code raises an exception
@test_case
def test_case_5() -> Union[bool, str]:
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
    # Check if the code raises an exception
    from response import add_ints

    try:
        result = add_ints(50, 25, 'string')
    except Exception as e:
        return True
    else:
        message = 'add_ints(50, 25, \'string\') expects an exception, but didn\'t get one.'
        return message

# Import response.py
try:
    import response
except Exception as e:
    print(e)
    print('JUDGE: response.py not found or unreadable')
else:
    import_failed = False
    print("JUDGE: Successfully found corresponding response.py!")
    print('_______________________________________\nTEST CASES:')
    run()