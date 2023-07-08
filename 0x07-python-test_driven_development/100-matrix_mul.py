#!/usr/bin/python3

"""Write a function that multiplies 2 matrices:"""


def matrix_mul(m_a, m_b):
    """This function computes matrix multiplication"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not (all(type(row) == list for row in m_a)):
        raise TypeError("m_a must be a list of lists")
    if not (all(type(row) == list for row in m_b)):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a[0] == []:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b[0] == []:
        raise ValueError("m_b can't be empty")
    if not (all(type(e) in [float, int] for e in [e for row in m_a for e in
                                                  row])):
        raise TypeError("m_a should contain only integers or floats")
    if not (all(type(e) in [float, int] for e in [e for row in m_b for e in
                                                  row])):
        raise TypeError("m_b should contain only integers or floats")
    if not (all(len(row) == len(m_a[0]) for row in m_a)):
        raise TypeError("each row of m_a must be of the same size")
    if not (all(len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError("each row of m_b must be of the same size")

    score = len(m_a[0])
    value = 0
    for row in m_b:
        value += 1

    if score != value:
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for a in range(len(m_a)):
        test = []
        for b in range(len(m_b[0])):
            c = 0
            for k in range(value):
                c += (m_a[a][k] * m_b[k][b])
            test.append(c)
        result.append(test)
    return (result)
