#!/usr/bin/python3
"""Defines a functions to multiply 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices
    Args:
        m_a: (list of lists of int(s) and float(s))
        m_b: (list of lists of int(s) and float(s))
    Raises:
            TypeError: if m_a or m_b is not a list or a list of lists
            ValueError: if m_a or m_b is empty or if the matrices cannot
            be multiplied
            TypeError: if any element of the matrices is not an int or a float
            TypeError: if m_a or m_b is have different row size
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    trans_b = []
    for rows in range(len(m_b[0])):
        new_rows = []
        for cols in range(len(m_b)):
            new_rows.append(m_b[cols][rows])
        trans_b.append(new_rows)
    res_matrix = []
    for row in m_a:
        new_rows = []
        for col in trans_b:
            result = 0
            for a in range(len(trans_b[0])):
                result += row[a] * col[a]
            new_rows.append(result)
        res_matrix.append(new_rows)

    return res_matrix
