#!/usr/bin/python3
"""This module prints a square made of number sign characters.

The public function validates the requested size and prints exactly that
many rows and columns.
"""


def print_square(size):
    """Print a square of '#' characters with side length size.

    The size must be a non-negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
