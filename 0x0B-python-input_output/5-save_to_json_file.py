#!/usr/bin/python3


"""Write a function that writes an Object to a text file,
using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """define save json file and initialize its return value"""
    with open(filename, 'w') as file:
        file_write = file.write(json.dumps(my_obj))
        return (file_write)
