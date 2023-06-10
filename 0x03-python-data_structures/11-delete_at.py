#!/usr/bin/python3

# Write a function that deletes the item at a specific position in a list.

def delete_at(my_list=None, idx=0):
    if my_list is None:
        my_list = []
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        for delete in range(len(my_list)):
            if delete == idx:
                my_list.remove(my_list[delete])
                return (my_list)
