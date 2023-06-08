#!/usr/bin/python3

from sys import argv

def length():

    print('{} argument'.format(len(argv) - 1), end='')

    if len(argv) == 1:
        print('s.')
    elif len(argv) == 2:
        print(':')
    else:
        print('s:')
    for axe in range(1, len(argv)):
        print('{}: {}'.format(axe, argv[axe]))

if __name__ == "__main__":
    length()
