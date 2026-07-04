#!/usr/bin/python3
"""This module provides a function that appends text to a file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
