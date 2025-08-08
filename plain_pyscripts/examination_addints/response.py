def add_ints(*args: int) -> int:
    """
    This function returns an integer sum of all passed integer arguments.

    Parameters:
        args: Multiple arguments, all of which must be integers

    Returns:
        an integer sum of all passed integer arguments
    
    >>> add_ints(5, 5)
    10
    >>> add_ints(6, -9)
    -3
    >>> add_ints(100, False)
    Traceback (most recent call last):
    ...
    AssertionError: Argument False is not integer
    """
    sum = 0
    for arg in args:
        assert isinstance(arg, int), f"Argument {arg} is not an integer"
        sum += arg
    return sum