#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces and element in a list in a specific location"""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    duplicate = [i for i in my_list]
    duplicate[idx] = element
    return duplicate
