#!/usr/bin/python3
"""This module provides a function that writes text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
