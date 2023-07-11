#!/usr/bin/pyhton3


"""Write a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added:"""


def append_write(filename="", text=""):
    """define append write function and return its value"""
    with open(filename, 'a') as file:
        file_append = file.write(text)
        return (file_append)
