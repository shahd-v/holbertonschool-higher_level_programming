#!/usr/bin/python3
"""Unit tests for the 6-max_integer module."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer with common and edge-case lists."""

    def test_ordered_list(self):
        """A sorted ascending list returns the last value."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """An unordered list returns the largest value."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """A list with the maximum first returns that first value."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_values(self):
        """A list of negative values returns the least negative value."""
        self.assertEqual(max_integer([-9, -3, -20]), -3)

    def test_single_value(self):
        """A one-item list returns its only value."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_repeated_maximum(self):
        """A repeated maximum value is still returned correctly."""
        self.assertEqual(max_integer([2, 8, 8, 1]), 8)


if __name__ == "__main__":
    unittest.main()
