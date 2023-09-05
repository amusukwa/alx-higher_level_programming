#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """
    multiplies two matrices

    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m-b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    # This is code above the blank line

    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiple")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
