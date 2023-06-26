#!/usr/bin/python3

# Write a function that executes a function safely.

def safe_function(fct, *args):
    try:
        safe = fct(*args)
        return (safe)
    except Exception as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
