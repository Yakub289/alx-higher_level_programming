#!/usr/bin/python3

# Write the Python function def magic_calculation(a, b):
#       that does exactly the same as the following Python bytecode:

def magic_calculation(a, b):
    result = 0
    for element in range(1, 3):
        try:
            if element > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / element
        except Exception:
            result = b + a
            break
    return (result)
