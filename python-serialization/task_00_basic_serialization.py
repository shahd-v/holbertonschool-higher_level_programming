#!/usr/bin/env python3
"""Provide helper functions for JSON dictionary serialization."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to JSON and save it to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it into a dictionary."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
