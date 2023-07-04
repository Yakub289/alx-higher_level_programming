#!/usr/bin/python3

"""Write a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """define matrix of sequence and return a new matrix case"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(field, list) for field in matrix) or
            not all((isinstance(record, int) or isinstance(record, float))
                    for record in [key for field in matrix for key in field])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(field) == len(matrix[0]) for field in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x/div, 2), field)) for field in matrix])
