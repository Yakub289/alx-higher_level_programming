#!/usr/bin/python3
def magic_string():
    iterate_magic_string = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool" for n in range(iterate_magic_string)])
