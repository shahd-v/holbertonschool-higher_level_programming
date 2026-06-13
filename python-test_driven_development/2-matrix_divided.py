#!/usr/bin/python3
"""This module divides every value in a numeric matrix by a number.

It validates matrix shape, matrix value types, and divisor safety before
returning a new matrix rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div.

    The original matrix is not modified.
    """
    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(type_msg)

    row_size = None
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(type_msg)
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(type_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
