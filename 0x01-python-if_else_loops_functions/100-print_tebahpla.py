#!/usr/bin/python3

# Write a program that prints the ASCII alphabet, in reverse order.

for reverse_order in range(ord("z"), ord("a") - 1, -1):
    if reverse_order % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(reverse_order - diff)), end="")
