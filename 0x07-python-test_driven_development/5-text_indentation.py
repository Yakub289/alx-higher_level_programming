#!/usr/bin/python3

"""Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """define text indentation"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    no_space = True
    size = 0
    text = text.strip()
    new_text = ""
    for character in text:
        if character == " " and character == no_space:
            pass
        elif character == "." or character == "?" or character == ":":
            new_text = new_text + character + "\n\n"
            no_space = True
        else:
            new_text = new_text + character
            no_space = False
    print(new_text, end="")
