from typing import List, Tuple, Union

def merge_in_ascending_order(
        collection1: Union[List[int | float], Tuple[int | float]],
        collection2: Union[List[int | float], Tuple[int | float]]
    ) -> Union[List[int | float], Tuple[int | float]]:
    """
    Merge two collections (tuples or lists), both already sorted in ascending order,
    into one single collection (tuple or list).

    Parameters:
        collection1: a tuple or list of only ints or floats in ascending order
        collection2: a tuple or list of only ints or floats in ascending order
    
    Returns:
        a tuple if both passed collections are tuples;
        a list otherwise.
    
    >>> merge_in_ascending_order([2, 3, 4], [2, 5, 7])
    [2, 2, 3, 4, 5, 7]
    >>> merge_in_ascending_order([-5, 3], (0, 0, 3))
    [-5, 0, 0, 3, 3]
    >>> merge_in_ascending_order((-0.5, 0), (-1,))
    (-1, -0.5, 0)
    >>> merge_in_ascending_order('str', (-1,))
    Traceback (most recent call last):
    ...
    AssertionError: collection1 passed is not a list nor a tuple
    >>> merge_in_ascending_order([-1], False)
    Traceback (most recent call last):
    ...
    AssertionError: collection2 passed is not a list nor a tuple
    >>> merge_in_ascending_order([2, 3, False], [2, 5, 7])
    Traceback (most recent call last):
    ...
    AssertionError: There is an element in one of the collections which is not an int nor a float (False)
    """
    assert isinstance(collection1, list) or isinstance(collection1, tuple), \
        "collection1 passed is not a list nor a tuple"
    assert isinstance(collection2, list) or isinstance(collection2, tuple), \
        "collection2 passed is not a list nor a tuple"

    merger = []
    index1 = 0
    index2 = 0
    while index1 < len(collection1) or index2 < len(collection2):
        if index1 < len(collection1) and index2 < len(collection2):
            assert isinstance(collection1[index1], int) or isinstance(collection1[index1], float), \
                f"There is an element in one of the collections which is not an int nor a float ({collection1[index1]})"
            assert isinstance(collection2[index2], int) or isinstance(collection2[index2], float), \
                f"There is an element in one of the collections which is not an int nor a float ({collection2[index2]})"
            if collection1[index1] <= collection2[index2]:
                merger.append(collection1[index1])
                index1 += 1
            else:
                merger.append(collection2[index2])
                index2 += 1
        elif index1 < len(collection1):
            assert isinstance(collection1[index1], int) or isinstance(collection1[index1], float), \
                f"There is an element in one of the collections which is not an int nor a float ({collection1[index1]})"
            merger.append(collection1[index1])
            index1 += 1
        elif index2 < len(collection2):
            assert isinstance(collection2[index2], int) or isinstance(collection2[index2], float), \
                f"There is an element in one of the collections which is not an int nor a float ({collection2[index2]})"
            merger.append(collection2[index2])
            index2 += 1

    if isinstance(collection1, tuple) and isinstance(collection2, tuple): # If both collections are tuples,
        return tuple(merger) # return a tuple.
    return merger # Otherwise, return a list

def merge_in_descending_order(
        collection1: Union[List[int | float], Tuple[int | float]],
        collection2: Union[List[int | float], Tuple[int | float]]
    ) -> Union[List[int | float], Tuple[int | float]]:
    """
    Merge two collections (tuples or lists), both already sorted in ascending order,
    into one single collection (tuple or list).

    Parameters:
        collection1: a tuple or list of only ints or floats in ascending order
        collection2: a tuple or list of only ints or floats in ascending order
    
    Returns:
        a tuple if both passed collections are tuples;
        a list otherwise.
    
    >>> merge_in_descending_order([4, 3, 2], [7, 5, 2])
    [7, 5, 4, 3, 2, 2]
    >>> merge_in_descending_order([-5, 3], (0, 0, 3))
    [3, 3, 0, 0, -5]
    >>> merge_in_descending_order((-0.5, 0), (-1,))
    (0, -0.5, -1)
    >>> merge_in_ascending_order('str', (-1,))
    Traceback (most recent call last):
    ...
    AssertionError: collection1 passed is not a list nor a tuple
    >>> merge_in_ascending_order([-1], False)
    Traceback (most recent call last):
    ...
    AssertionError: collection2 passed is not a list nor a tuple
    >>> merge_in_ascending_order([2, 3, False], [2, 5, 7])
    Traceback (most recent call last):
    ...
    AssertionError: There is an element in one of the collections which is not an int nor a float (False)
    """
    assert isinstance(collection1, list) or isinstance(collection1, tuple), \
        "collection1 passed is not a list nor a tuple"
    assert isinstance(collection2, list) or isinstance(collection2, tuple), \
        "collection2 passed is not a list nor a tuple"
    
    merger = []
    index1 = 0
    index2 = 0
    while index1 < len(collection1) or index2 < len(collection2):
        if index1 < len(collection1) and index2 < len(collection2):
            assert isinstance(collection1[index1], int) or isinstance(collection1[index1], float), \
                f"There is an element in one of the collections which is not an int nor a float ({collection1[index1]})"
            assert isinstance(collection2[index2], int) or isinstance(collection2[index2], float), \
                f"There is an element in one of the collections which is not an int nor a float ({collection2[index2]})"
            if collection1[index1] <= collection2[index2]:
                merger.append(collection1[index1])
                index1 += 1
            else:
                merger.append(collection2[index2])
                index2 += 1
        elif index1 < len(collection1):
            assert isinstance(collection1[index1], int) or isinstance(collection1[index1], float), \
                f"There is an element in one of the collections which is not an int nor a float ({collection1[index1]})"
            merger.append(collection1[index1])
            index1 += 1
        elif index2 < len(collection2):
            assert isinstance(collection2[index2], int) or isinstance(collection2[index2], float), \
                f"There is an element in one of the collections which is not an int nor a float ({collection2[index2]})"
            merger.append(collection2[index2])
            index2 += 1

    if isinstance(collection1, tuple) and isinstance(collection2, tuple): # If both collections are tuples,
        return tuple(merger) # return a tuple.
    return merger # Otherwise, return a list

def ascending_insertion_sort(collection: Union[List[int | float], Tuple[int | float]]) -> Union[List[int | float], Tuple[int | float]]:
    """
    This function sorts either lists or tuples comprising of only numeric values in ascending order
    using the insertion sort algorithm.
    
    It will not modify the original collection.

    Parameters:
        collection: a list or a tuple of only numeric values
    
    Returns:
        a sorted list if the passed collection is a list, a sorted tuple if a tuple
    
    >>> ascending_insertion_sort([5, 3, 2, 1, -100, 5, 7, 0])
    [-100, 0, 1, 2, 3, 5, 5, 7]
    >>> ascending_insertion_sort((-1, 2, 3, -3, 3, 3,))
    (-3, -1, 2, 3, 3, 3)
    >>> ascending_insertion_sort([0, 0, True, 'string'])
    Traceback (most recent call last):
    ...
    AssertionError: True is a non-numeric value in the passed collection
    >>> ascending_insertion_sort('placeholder')
    Traceback (most recent call last):
    ...
    AssertionError: collection is not a list nor a tuple.
    """

    assert isinstance(collection, list) or isinstance(collection, tuple), \
        "collection is not a list nor a tuple"
    
    if len(collection) == 0:
        return collection
    
    if len(collection) == 1:
        assert isinstance(collection[0], int) or isinstance(collection[0], float), \
            f"{collection[0]} is a non-numeric value in the passed collection"
        return collection
    
    copy = list(collection).copy()

    assert isinstance(copy[0], int) or isinstance(copy[0], float), \
        f"{copy[0]} is a non-numeric value in the passed collection"

    # Insertion sort
    for i in range(1, len(copy)):
        assert isinstance(copy[i], int) or isinstance(copy[i], float), \
            f"{copy[i]} is a non-numeric value in the passed collection"
        
        temp = copy[i]

        j = i - 1
        while j >= 0 and temp < copy[j]:
            copy[j + 1] = copy[j]
            j -= 1
        copy[j + 1] = temp
    
    if isinstance(collection, tuple):
        return tuple(copy) # Return a tuple
    return list(copy) # Return a list otherwise

def descending_insertion_sort(collection: Union[List[int | float], Tuple[int | float]]) -> Union[List[int | float], Tuple[int | float]]:
    """
    This function sorts either lists or tuples comprising of only numeric values in descending order
    using the insertion sort algorithm.
    
    It will not modify the original collection.

    Parameters:
        collection: a list or a tuple of only numeric values
    
    Returns:
        a sorted list if the passed collection is a list, a sorted tuple if a tuple
    
    >>> descending_insertion_sort([5, 3, 2, 1, -100, 5, 7, 0])
    [7, 5, 5, 3, 2, 1, 0, -100]
    >>> descending_insertion_sort((-1, 2, 3, -3, 3, 3,))
    (3, 3, 3, 2, -1, -3)
    >>> descending_insertion_sort([0, 0, True, 'string'])
    Traceback (most recent call last):
    ...
    AssertionError: True is a non-numeric value in the passed collection
    >>> descending_insertion_sort('placeholder')
    Traceback (most recent call last):
    ...
    AssertionError: collection is not a list nor a tuple.
    """

    assert isinstance(collection, list) or isinstance(collection, tuple), \
        "collection is not a list nor a tuple"
    
    if len(collection) == 0:
        return collection
    
    if len(collection) == 1:
        assert isinstance(collection[0], int) or isinstance(collection[0], float), \
            f"{collection[0]} is a non-numeric value in the passed collection"
        return collection
    
    copy = list(collection).copy()

    assert isinstance(copy[-1], int) or isinstance(copy[-1], float), \
        f"{copy[-1]} is a non-numeric value in the passed collection"

    # Insertion sort
    for i in range(-2, -len(copy)-1, -1):
        assert isinstance(copy[i], int) or isinstance(copy[i], float), \
            f"{copy[i]} is a non-numeric value in the passed collection"
        
        temp = copy[i]

        j = i + 1
        while j <= -1 and temp < copy[j]:
            copy[j - 1] = copy[j]
            j += 1
        copy[j - 1] = temp

    if isinstance(collection, tuple):
        return tuple(copy) # Return a tuple
    return list(copy) # Return a list otherwise

def ascending_binary_search(x: int | float, collection: Union[List[int | float], Tuple[int | float]]) -> int:
    """
    Returns the index of a number in a collection sorted in ascending order.

    Parameters:
        x: the number
        collection: a list or a tuple of ints or floats already sorted in ascending order

    Returns:
        the index of x in collection, which is already sorted in ascending order.
        -1 if x cannot be found in collection.
    """
    assert isinstance(x, int) or isinstance(x, float), f"x ({x}) is not an int or a float"
    assert isinstance(collection, list) or isinstance(collection, tuple), \
        "collection is not a list nor a tuple"
    
    min = 0
    max = len(collection) - 1
    while (min <= max):
        assert isinstance(collection[min], int) or isinstance(collection[min], float), \
            f"There is a non-numeric element in collection, which is {collection[min]}"
        assert isinstance(collection[max], int) or isinstance(collection[max], float), \
            f"There is a non-numeric element in collection, which is {collection[min]}"
        mid = (min + max) // 2
        assert isinstance(collection[mid], int) or isinstance(collection[mid], float), \
            f"There is a non-numeric element in collection, which is {collection[min]}"
        if (collection[mid] == x):
            return mid
        elif (x < collection[mid]):
            max = mid - 1
        else: # x > collection[mid]
            min = mid + 1
    return -1

def descending_binary_search(x: int | float, collection: Union[List[int | float], Tuple[int | float]]) -> int:
    """
    Returns the index of a number in a collection sorted in descending order.

    Parameters:
        x: the number
        collection: a list or a tuple of ints or floats already sorted in descending order

    Returns:
        the index of x in collection, which is already sorted in descending order.
        -1 if x cannot be found in collection.
    """
    assert isinstance(x, int) or isinstance(x, float), f"x ({x}) is not an int or a float"
    assert isinstance(collection, list) or isinstance(collection, tuple), \
        "collection is not a list nor a tuple"
    
    min = 0
    max = len(collection) - 1
    while (min <= max):
        assert isinstance(collection[min], int) or isinstance(collection[min], float), \
            f"There is a non-numeric element in collection, which is {collection[min]}"
        assert isinstance(collection[max], int) or isinstance(collection[max], float), \
            f"There is a non-numeric element in collection, which is {collection[min]}"
        mid = (min + max) // 2
        assert isinstance(collection[mid], int) or isinstance(collection[mid], float), \
            f"There is a non-numeric element in collection, which is {collection[min]}"
        if (collection[mid] == x):
            return mid
        elif (x > collection[mid]):
            max = mid - 1
        else: # x < collection[mid]
            min = mid + 1
    return -1

def sort_and_search(x: int | float, collection: Union[List[int | float], Tuple[int | float]]) -> int:
    """
    This function sorts a collection in ascending order using insertion sort and searches for a number's index in that
    collection with binary search.

    Parameters:
        x: the number
        collection: a list or a tuple of ints or floats

    Returns:
        the index of x in collection if it can be found.
        -1 if x cannot be found in collection.
    """
    sorted = ascending_insertion_sort(collection)
    return ascending_binary_search(x, sorted)