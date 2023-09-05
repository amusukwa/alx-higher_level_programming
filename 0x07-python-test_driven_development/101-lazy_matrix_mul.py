#!/usr/bin/python3
""""
This function multiplies two matrices
using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    """
    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)

    try:
        result = np.dot(np_m_a, np_m_b)
        return result
    except ValueError:
        raise ValueError("Matrices cannot be multiplied")
