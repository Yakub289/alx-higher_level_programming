#!/usr/bin/python3

# Write a function that returns the weighted average of all integers tuple.

def weight_average(my_list=[]):
    if my_list and len(my_list):
        score = 0
        weight = 0
        for tup in my_list:
            score += (tup[0] * tup[1])
            weight += (tup[1])
        return (score/weight)
    return 0
