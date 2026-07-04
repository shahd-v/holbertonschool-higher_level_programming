#!/usr/bin/python3
"""This module provides a function that saves objects as JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
