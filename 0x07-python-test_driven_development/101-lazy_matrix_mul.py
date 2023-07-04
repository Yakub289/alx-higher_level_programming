#!/usr/bin/python3

"""Write a function that multiplies 2 matrices by using the module NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """define lazy matrix multiples"""
    return (np.matmul(m_a, m_b))
