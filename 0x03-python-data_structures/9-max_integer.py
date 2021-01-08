#!/usr/bin/python3
def max_integer(my_list=[]):
    """Returns the biggest value in a list of integers"""
    if len(my_list) == 0:
        return None
    maxint = my_list[0]
    for idx in range(len(my_list)):
        if my_list[idx] > maxint:
            maxint = my_list[idx]
    return maxint
