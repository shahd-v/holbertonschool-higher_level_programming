#!/usr/bin/python3
"""This module finds the maximum integer in a list.

It is intentionally small so unittest coverage can focus on edge cases like
empty lists, negative values, and repeated maximum values.
"""


def max_integer(list=[]):
    """Return the maximum integer in list, or None for an empty list.

    The function walks the list manually instead of using max.
    """
    if list == []:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
