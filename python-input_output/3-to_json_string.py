#!/usr/bin/python3
"""This module provides a function that serializes objects to JSON text."""

import json


def to_json_string(my_obj):
    """Return the JSON string representation of a Python object."""
    return json.dumps(my_obj)
