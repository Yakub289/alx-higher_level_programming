#!/usr/bin/python3


"""Write a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, 'r') as file:
        file_content = file.read()
    print(file_content, end="")
