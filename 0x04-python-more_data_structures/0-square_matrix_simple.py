#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_row = []
    for simple in range(len(matrix)):
        for square in range(len(matrix[simple])):
            new_row.append(matrix[simple][square] ** 2)
        new_matrix.append(new_row)
        new_row = []
    return (new_matrix)
