#!/usr/bin/python3
"""Define a Square class that can compute its area."""


class Square:
    """Represent a square with validated size and area behavior."""

    def __init__(self, size=0):
        """Initialize a square after validating its size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
