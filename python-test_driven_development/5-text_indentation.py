#!/usr/bin/python3
"""This module formats text by inserting blank lines after punctuation.

The public function demonstrates careful string traversal, validation, and
stdout behavior that can be verified with doctest.
"""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':' characters.

    Leading spaces after punctuation are skipped.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False
    for char in text:
        if skip_space and char == " ":
            continue
        skip_space = False
        print(char, end="")
        if char in ".?:":
            print("\n")
            skip_space = True
