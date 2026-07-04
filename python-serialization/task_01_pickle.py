#!/usr/bin/env python3
"""Define a custom object that can be serialized with pickle."""

import pickle


class CustomObject:
    """Represent a simple object with student-related attributes."""

    def __init__(self, name, age, is_student):
        """Initialize a custom object with a name, age, and student flag."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object instance to a pickle file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return a CustomObject instance from a file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (OSError, EOFError, pickle.PickleError):
            return None
