#!/usr/bin/python3
"""This module provides integer addition with basic type validation.

It exposes one function, add_integer, which accepts integers or floats,
casts accepted values to integers, and returns their sum.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b after validating their types.

    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
