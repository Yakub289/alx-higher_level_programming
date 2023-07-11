#!/usr/bin/python3


"""Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):"""


def append_after(filename="", search_string="", new_string=""):
    """define the append list through str at each line"""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
