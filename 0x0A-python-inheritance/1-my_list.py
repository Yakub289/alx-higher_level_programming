#!/usr/bin/python3


"""Write a class MyList that inherits from list:"""


class MyList(list):
    """Class definition and sub-divide in unit"""
    def print_sorted(self):
        """define print_sort and print all list in ascending order"""
        print(sorted(self))
