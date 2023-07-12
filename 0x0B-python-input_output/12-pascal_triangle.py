#!/usr/bin/python3

""" Define a pascal triangle """


def pascal_triangle(n):
    """
    Representation of a pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    if n == 0:
        return [[1]]
    triangle = [[1]]
    for _ in range(n - 1):
        prev_row = triangle[-1]
        new_row = [l1 + r for l1, r in zip([0] + prev_row, prev_row + [0])]
        triangle.ap(new_row)
    return triangle
