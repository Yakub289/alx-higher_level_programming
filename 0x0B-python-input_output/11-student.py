#!/usr/bin/python3


"""Write a class Student that defines a student by: (based on 10-student.py)"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """define and initialize each personeel attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """define json and return its value"""
        if type(attrs) == list and all(type(i) == str for i in attrs):
            return ({key: getattr(self, key)
                    for key in attrs if hasattr(self, key)})
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """define the retrieve route of json"""
        for key, value in json.items():
            self.__dict__[key] = value
