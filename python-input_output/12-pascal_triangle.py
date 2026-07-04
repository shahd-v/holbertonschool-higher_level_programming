#!/usr/bin/python3
"""This module provides a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of size n."""
    triangle = []

    if n <= 0:
        return triangle

    for row_index in range(n):
        row = [1] * (row_index + 1)

        for col_index in range(1, row_index):
            row[col_index] = (
                triangle[row_index - 1][col_index - 1] +
                triangle[row_index - 1][col_index]
            )

        triangle.append(row)

    return triangle
