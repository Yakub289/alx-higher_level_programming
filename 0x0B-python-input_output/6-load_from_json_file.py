#!/usr/bin/python3


"""Write a function that creates an Object from a “JSON file”:"""
import json


def load_from_json_file(filename):
    """define load from json file and return and its value"""
    with open(filename, 'r') as file:
        fetch_file = json.load(file)
        return (fetch_file)
