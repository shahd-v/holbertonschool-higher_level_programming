#!/usr/bin/python3
"""Define a Rectangle class that counts active instances."""


class Rectangle:
    """Represent a rectangle while tracking instance count."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle and increment the instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the current rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width after validating it."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the current rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height after validating it."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or zero if empty."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a hash-character drawing of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return a string representation able to recreate the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement the instance counter on deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
