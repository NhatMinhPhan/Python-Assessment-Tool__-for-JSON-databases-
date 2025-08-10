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
    results.append(test_case_2() == True)
    results.append(test_case_3() == True)
    results.append(test_case_4() == True)
    results.append(test_case_5() == True)
    results.append(test_case_6() == True)
    results.append(test_case_7() == True)
    results.append(test_case_8() == True)
    results.append(test_case_9() == True)
    results.append(test_case_10() == True)
    results.append(test_case_11() == True)
    results.append(test_case_12() == True)
    results.append(test_case_13() == True)
    results.append(test_case_14() == True)
    results.append(test_case_15() == True)
    results.append(test_case_16() == True)
    results.append(test_case_17() == True)
    results.append(test_case_18() == True)
    results.append(test_case_19() == True)
    results.append(test_case_20() == True)
    results.append(test_case_21() == True)
    results.append(test_case_22() == True)
    results.append(test_case_23() == True)
    results.append(test_case_24() == True)
    results.append(test_case_25() == True)
    results.append(test_case_26() == True)
    
    test_ok: bool = False not in results
    if test_ok:
        print('TEST OK\n_______________________________________')
    else:
        fails = results.count(False) # when test_case() != True
        fail_percentage = round(fails/len(results)*100, 2)
        print(f'Failed {fails}/{len(results)} cases ({fail_percentage}%).\n_______________________________________')
    return test_ok

# ascending_insertion_sort
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
    from response import ascending_insertion_sort

    collection = [5, 3, 2, -1, 100, 2.2, 5.5]
    expected = [-1, 2, 2.2, 3, 5, 5.5, 100]

    try:
        result = ascending_insertion_sort(collection)
    except Exception as e:
        message = f'ascending_insertion_sort({collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'ascending_insertion_sort({collection}) expects {expected}, but got {result}'
        return message
    return True

# ascending_insertion_sort
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
    from response import ascending_insertion_sort

    collection = [1, 2, 4, 3, 5, 6, 7, 8, 9, 0]
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    try:
        result = ascending_insertion_sort(collection)
    except Exception as e:
        message = f'ascending_insertion_sort({collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'ascending_insertion_sort({collection}) expects {expected}, but got {result}'
        return message
    return True

# ascending_insertion_sort
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
    from response import ascending_insertion_sort

    collection = (1,)
    expected = (1,)

    try:
        result = ascending_insertion_sort(collection)
    except Exception as e:
        message = f'ascending_insertion_sort({collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'ascending_insertion_sort({collection}) expects {expected}, but got {result}'
        return message
    return True

# descending_insertion_sort
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
    from response import descending_insertion_sort

    collection = [5, 3, 2, -1, 100, 2.2, 5.5]
    expected = [100, 5.5, 5, 3, 2.2, 2, -1]

    try:
        result = descending_insertion_sort(collection)
    except Exception as e:
        message = f'descending_insertion_sort({collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'descending_insertion_sort({collection}) expects {expected}, but got {result}'
        return message
    return True

# descending_insertion_sort
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
    from response import descending_insertion_sort

    collection = (1, 2, 4, 3, 5, 6, 7, 8, 9, 0)
    expected = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

    try:
        result = descending_insertion_sort(collection)
    except Exception as e:
        message = f'descending_insertion_sort({collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'descending_insertion_sort({collection}) expects {expected}, but got {result}'
        return message
    return True

# descending_insertion_sort
@test_case
def test_case_6() -> Union[bool, str]:
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
    from response import descending_insertion_sort

    collection = (-100,)
    expected = (-100,)

    try:
        result = descending_insertion_sort(collection)
    except Exception as e:
        message = f'descending_insertion_sort({collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'descending_insertion_sort({collection}) expects {expected}, but got {result}'
        return message
    return True

# This test case examines if the code raises an exception - descending_insertion_sort
@test_case
def test_case_7() -> Union[bool, str]:
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
    from response import descending_insertion_sort

    collection = '(1, 2, 4, 3, 5, 6, 7, 8, 9, 0)'

    # Check if the code raises an exception

    try:
        result = descending_insertion_sort(collection)
    except Exception as e:
        return True
    else:
        message = f'descending_insertion_sort({collection}) expects an exception, but didn\'t get one'
        return message

# This test case examines if the code raises an exception - ascending_insertion_sort
@test_case
def test_case_8() -> Union[bool, str]:
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
    from response import ascending_insertion_sort

    collection = (1, (2, 3), 4, 5, 6)

    # Check if the code raises an exception

    try:
        result = ascending_insertion_sort(collection)
    except Exception as e:
        return True
    else:
        message = f'ascending_insertion_sort({collection}) expects an exception, but didn\'t get one'
        return message

# merge_in_ascending_order
@test_case
def test_case_9() -> Union[bool, str]:
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
    from response import merge_in_ascending_order

    collection1 = [2, 3, 5]
    collection2 = [2.1, 2.2, 5.1]
    expected = [2, 2.1, 2.2, 3, 5, 5.1]

    try:
        result = merge_in_ascending_order(collection1, collection2)
    except Exception as e:
        message = f'merge_in_ascending_order({collection1}, {collection2}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'merge_in_ascending_order({collection1}, {collection2}) expects {expected}, but got {result}'
        return message
    return True

# merge_in_ascending_order
@test_case
def test_case_10() -> Union[bool, str]:
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
    from response import merge_in_ascending_order

    collection1 = (-100, -98, -5, 3)
    collection2 = [2.1, 2.2, 5.1]
    expected = [-100, -98, -5, 2.1, 2.2, 3, 5.1]

    try:
        result = merge_in_ascending_order(collection1, collection2)
    except Exception as e:
        message = f'merge_in_ascending_order({collection1}, {collection2}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'merge_in_ascending_order({collection1}, {collection2}) expects {expected}, but got {result}'
        return message
    return True

# merge_in_ascending_order
@test_case
def test_case_11() -> Union[bool, str]:
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
    from response import merge_in_ascending_order

    collection1 = (-1, 0, 1)
    collection2 = (0, 1, 1.1, 2, 3)
    expected = (-1, 0, 0, 1, 1, 1.1, 2, 3)

    try:
        result = merge_in_ascending_order(collection1, collection2)
    except Exception as e:
        message = f'merge_in_ascending_order({collection1}, {collection2}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'merge_in_ascending_order({collection1}, {collection2}) expects {expected}, but got {result}'
        return message
    return True

# merge_in_descending_order
@test_case
def test_case_12() -> Union[bool, str]:
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
    from response import merge_in_descending_order

    collection1 = (1, 0, -1, -1)
    collection2 = (3, 2, 1.1, 1, 0)
    expected = (3, 2, 1.1, 1, 1, 0, 0, -1, -1)

    try:
        result = merge_in_descending_order(collection1, collection2)
    except Exception as e:
        message = f'merge_in_descending_order({collection1}, {collection2}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'merge_in_descending_order({collection1}, {collection2}) expects {expected}, but got {result}'
        return message
    return True

# merge_in_descending_order
@test_case
def test_case_13() -> Union[bool, str]:
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
    from response import merge_in_descending_order

    collection1 = [1, 1, -100]
    collection2 = (3, 2, 1.1, 1, 0)
    expected = [3, 2, 1.1, 1, 1, 1, 0, -100]

    try:
        result = merge_in_descending_order(collection1, collection2)
    except Exception as e:
        message = f'merge_in_descending_order({collection1}, {collection2}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'merge_in_descending_order({collection1}, {collection2}) expects {expected}, but got {result}'
        return message
    return True

# This test case examines if the code raises an exception - merge_in_ascending_order
@test_case
def test_case_14() -> Union[bool, str]:
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
    from response import merge_in_ascending_order

    collection1 = (1, (2, 3), 4, 5, 6)
    collection2 = False

    # Check if the code raises an exception

    try:
        result = merge_in_ascending_order(collection1, collection2)
    except Exception as e:
        return True
    else:
        message = f'merge_in_ascending_order({collection1}, {collection2}) expects an exception, but didn\'t get one (returned {result})'
        return message

# This test case examines if the code raises an exception - merge_in_descending_order
@test_case
def test_case_15() -> Union[bool, str]:
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
    from response import merge_in_descending_order

    collection1 = (6, 5, 4, 2, 1)
    collection2 = [4, False, 3, 1]

    # Check if the code raises an exception

    try:
        result = merge_in_descending_order(collection1, collection2)
    except Exception as e:
        return True
    else:
        message = f'merge_in_descending_order({collection1}, {collection2}) expects an exception, but didn\'t get one (returned {result})'
        return message

# ascending_binary_search
@test_case
def test_case_16() -> Union[bool, str]:
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
    from response import ascending_binary_search

    collection = (-1, 0, 0, 1, 1, 1.1, 2, 3)
    x = 2
    expected = 6

    try:
        result = ascending_binary_search(x, collection)
    except Exception as e:
        message = f'ascending_binary_search({x}, {collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'ascending_binary_search({x}, {collection}) expects {expected}, but got {result}'
        return message
    return True

# ascending_binary_search
@test_case
def test_case_17() -> Union[bool, str]:
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
    from response import ascending_binary_search

    collection = [-100, -95, -64, -31, -29, -0.03, 0, 1.2, 4.5, 8.8, 10, 10.9, 11, 58]
    x = 1.2
    expected = 7

    try:
        result = ascending_binary_search(x, collection)
    except Exception as e:
        message = f'ascending_binary_search({x}, {collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'ascending_binary_search({x}, {collection}) expects {expected}, but got {result}'
        return message
    return True

# ascending_binary_search
@test_case
def test_case_18() -> Union[bool, str]:
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
    from response import ascending_binary_search

    collection = (-100, -95, -64, -31, -29, -0.03, 0, 1.2, 4.5, 8.8, 10, 10.9, 11, 58)
    x = 2
    expected = -1

    try:
        result = ascending_binary_search(x, collection)
    except Exception as e:
        message = f'ascending_binary_search({x}, {collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'ascending_binary_search({x}, {collection}) expects {expected}, but got {result}'
        return message
    return True

# ascending_binary_search
@test_case
def test_case_19() -> Union[bool, str]:
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
    from response import ascending_binary_search

    collection = [-100, -95, -64, -31, -29, -0.03, 0, 1.2, 4.5, 8.8, 10, 10.9, 11, 58]
    x = -28
    expected = -1

    try:
        result = ascending_binary_search(x, collection)
    except Exception as e:
        message = f'ascending_binary_search({x}, {collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'ascending_binary_search({x}, {collection}) expects {expected}, but got {result}'
        return message
    return True

# This test case examines if the code raises an exception - ascending_binary_search
@test_case
def test_case_20() -> Union[bool, str]:
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
    from response import ascending_binary_search

    collection = [-100, -95, -64, -31, -29, -0.03, 0, 1.2, 4.5, 8.8, 10, 10.9, 11, 58]
    x = False

    # Check if the code raises an exception

    try:
        result = ascending_binary_search(x, collection)
    except Exception as e:
        return True
    else:
        message = f'ascending_binary_search({x}, {collection}) expects an exception, but didn\'t get one'
        return message

# This test case examines if the code raises an exception - ascending_binary_search
@test_case
def test_case_21() -> Union[bool, str]:
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
    from response import ascending_binary_search

    collection = {1, 2, 3, 5}
    x = 5

    # Check if the code raises an exception

    try:
        result = ascending_binary_search(x, collection)
    except AssertionError as e:
        return True
    except Exception as e:
        exception_type = str(e)
        message = f'ascending_binary_search({x}, {collection}) expects the wrong exception ({exception_type})'
        return message
    else:
        message = f'ascending_binary_search({x}, {collection}) expects an exception, but didn\'t get one'
        return message

# descending_binary_search
@test_case
def test_case_22() -> Union[bool, str]:
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
    from response import descending_binary_search

    collection = (3, 2, 1.1, 1, 1, 0, 0, -1)
    x = 2
    expected = 1

    try:
        result = descending_binary_search(x, collection)
    except Exception as e:
        message = f'descending_binary_search({x}, {collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'descending_binary_search({x}, {collection}) expects {expected}, but got {result}'
        return message
    return True

# descending_binary_search
@test_case
def test_case_23() -> Union[bool, str]:
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
    from response import descending_binary_search

    collection = [100, 5.5, 5.4, 5.3, 5, 4.9, 4.7, 3, 2.1111, 2.1, 2.09, 1, 0.1, -0.9, -1, -2.5, -10]
    x = 1
    expected = 11

    try:
        result = descending_binary_search(x, collection)
    except Exception as e:
        message = f'descending_binary_search({x}, {collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'descending_binary_search({x}, {collection}) expects {expected}, but got {result}'
        return message
    return True

# descending_binary_search
@test_case
def test_case_24() -> Union[bool, str]:
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
    from response import descending_binary_search

    collection = (100, 5.5, 5.4, 5.3, 5, 4.9, 4.7, 3, 2.1111, 2.1, 2.09, 1, 0.1, -0.9, -1, -2.5, -10)
    x = -10.5
    expected = -1

    try:
        result = descending_binary_search(x, collection)
    except Exception as e:
        message = f'descending_binary_search({x}, {collection}) expects a result, but got an exception: {str(e).capitalize()}'
        return message

    if expected != result:
        message = f'descending_binary_search({x}, {collection}) expects {expected}, but got {result}'
        return message
    return True

# This test case examines if the code raises an exception - descending_binary_search
@test_case
def test_case_25() -> Union[bool, str]:
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
    from response import descending_binary_search

    collection = {5,3,2,1}
    x = 5

    # Check if the code raises an exception

    try:
        result = descending_binary_search(x, collection)
    except AssertionError as e:
        return True
    except Exception as e:
        exception_type = str(e)
        message = f'descending_binary_search({x}, {collection}) expects the wrong exception ({exception_type})'
        return message
    else:
        message = f'descending_binary_search({x}, {collection}) expects an exception, but didn\'t get one'
        return message
    
# This test case examines if the code raises an exception - descending_binary_search
@test_case
def test_case_26() -> Union[bool, str]:
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
    from response import descending_binary_search

    collection = (5,3,2,1)
    x = True

    # Check if the code raises an exception

    try:
        result = descending_binary_search(x, collection)
    except AssertionError as e:
        return True
    except Exception as e:
        exception_type = str(e)
        message = f'descending_binary_search({x}, {collection}) expects the wrong exception ({exception_type})'
        return message
    else:
        message = f'descending_binary_search({x}, {collection}) expects an exception, but didn\'t get one'
        return message

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