#!/usr/bin/python3


"""Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n:"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n"""

    list_lists = []
    if n <= 0:
        return (list_lists)

    for pyramid in range(n):
        row = [1]
        if i > 0:
            for prime in range(pyramid):
                row.append(sum(list[-1][prime:prime + 2]))
        list_lists.append(row)
    return (list_lists)
