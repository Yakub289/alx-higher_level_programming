#!/usr/bin/python3

# Write a function that divides element by element 2 lists.

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for elements in range(list_length):
        try:
            divides = my_list_1[elements] / my_list_2[elements]
        except (ValueError, TypeError):
            print("wrong type")
            divides = 0
        except ZeroDivisionError:
            print("division by 0")
            divides = 0
        except IndexError:
            print("out of range")
            divides = 0
        finally:
            new_list.append(divides)
    return (new_list)
