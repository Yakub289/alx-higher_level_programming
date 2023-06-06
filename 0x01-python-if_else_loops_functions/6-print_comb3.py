#!/usr/bin/python3
for unique_digits in range(1, 90):
    if unique_digits / 10 > unique_digits % 10:
        continue

    else:
        if (unique_digits != 89):
            print("{:02d}".format(unique_digits), end=", ")
        else:
            print("{}".format(unique_digits))
