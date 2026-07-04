#!/usr/bin/python3
"""This module provides a function that reads and prints a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its full contents to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
