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

if __name__ == "__main__":
    # Example usage
    m_a = [[1, 2], [3, 4]]
    m_b = [[5, 6], [7, 8]]
    result = lazy_matrix_mul(m_a, m_b)
    print(result)

