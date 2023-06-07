#!/usr/bin/python3

# (not the Python way, the “C array index”).

def remove_char_at(str, p):
    if p < 0:
        return (str)
    return (str[:p] + str[p+1:])
