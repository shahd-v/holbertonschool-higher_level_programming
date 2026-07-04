#!/usr/bin/python3
"""This module defines a Student class for JSON serialization practice."""


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student with identity fields and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of this student instance."""
        return self.__dict__
