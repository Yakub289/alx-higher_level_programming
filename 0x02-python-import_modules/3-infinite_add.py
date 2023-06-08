#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    count = len(sys.argv) - 1
    sum = 0
    for map in range(count):
        sum = sum + int(sys.argv[map + 1])
    print("{}".format(sum))
