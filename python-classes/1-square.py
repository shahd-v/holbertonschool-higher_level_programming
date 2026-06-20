#!/usr/bin/python3
"""Define a Square class with a private size attribute."""


class Square:
    """Represent a square with a stored private size."""

    def __init__(self, size):
        """Initialize a square with the provided size."""
        self.__size = size
