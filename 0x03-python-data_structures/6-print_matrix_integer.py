#!/usr/bin/python3

# Write a function that prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    for field in range(len(matrix)):
        for record in range(len(matrix[field])):
            if record != len(matrix[field]) - 1:
                print("{:d}".format(matrix[field][record]), end=" ")
            else:
                print("{:d}".format(matrix[field][record]), end="")
        print("")
