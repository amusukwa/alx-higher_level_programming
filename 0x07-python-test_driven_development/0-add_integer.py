#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers

    Examples:
        >>> add_integer(5, 10)
        15
        >>> add_integer(3.5, 4)
        7
        >>> add_integer(5, 3.5)
        8
    """
    return int(a) + int(b)
