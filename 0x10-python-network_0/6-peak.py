#!/usr/bin/python3

"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Args:list_of_integers(int).
    Returns: peak of list_of_integers or None.
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
