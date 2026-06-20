#!/usr/bin/python3
"""Define a Square class with validated size."""


class Square:
    """Represent a square whose size is validated at creation."""

    def __init__(self, size=0):
        """Initialize a square after validating its size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
