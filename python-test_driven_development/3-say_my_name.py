#!/usr/bin/python3
"""This module prints a formatted name after validating both name values.

It exposes say_my_name, a small helper used to demonstrate type checking
and output testing with doctest.
"""


def say_my_name(first_name, last_name=""):
    """Print a sentence containing first_name and last_name.

    Both arguments must be strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
