#!/usr/bin/python3


"""Write a class Student that defines a student by:"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """define and initialize each personeel attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """define json and return its value"""
        return (self.__dict__)
