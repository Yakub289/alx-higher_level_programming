#!/usr/bin/python3


"""Write a function that writes a string to a text file (UTF8)
and returns the number of characters written:"""


def write_file(filename="", text=""):
    """define the write function and return it value"""
    with open(filename, 'w') as file:
        file_write = file.write(text)
    return (file_write)
