#!/usr/bin/python3

# 2-matrix_divided.py
""" Defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Args:
        matrix: a matrix of int(s) or float(s)
        div: num to divide the matrix elements by.
    Raises:
            TypeError: If matrix is not a matrix of int(s) or float(s)
            or if div is not a num.
            TypeError: If each row of the matrix does not have the same size.
            ZeroDivisionError: If div is equal to 0
    Retruns:
            New matrix with all elements divides by div, rounded to 2 dp
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(elem, int) or isinstance(elem, float)
                for elem in [i for row in matrix for i in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matr = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matr
