def add_ints(*args: int) -> int:
    """
    This function returns an integer sum of all passed integer arguments.

    Parameters:
        args: Multiple arguments, all of which must be integers

    Returns:
        an integer sum of all passed integer arguments
    """
    sum = 0
    for arg in args:
        assert isinstance(arg, int), f"Argument {arg} is not an integer"
        sum += arg
    return sum