#!/usr/bin/python3
"""This module provides a function that loads objects from JSON files."""

import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
