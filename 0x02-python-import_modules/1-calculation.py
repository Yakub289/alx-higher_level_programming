#!/usr/bin/python3

# The value 10 to a variable a
# The value 5 to a variable b

if __name__ == "__main__":

    from calculator_1 import add, div, mul, sub

    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, (add(a, b))))
    print("{:d} - {:d} = {:d}".format(a, b, (sub(a, b))))
    print("{:d} * {:d} = {:d}".format(a, b, (mul(a, b))))
    print("{:d} / {:d} = {:d}".format(a, b, (div(a, b))))
