#!/usr/bin/python3
"""This module provides a function that exposes an object's attributes."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON encoding."""
    return obj.__dict__
