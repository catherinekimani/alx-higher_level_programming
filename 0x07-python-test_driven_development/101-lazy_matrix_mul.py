#!/usr/bin/python3
# 101-lazy_matrix_mul.py
""" Defines a function that multiplies 2 matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrices using numpy
    Args:
        m_a: first matrix
        m_b: second matrix
    """
    return np.matmul(m_a, m_b)
