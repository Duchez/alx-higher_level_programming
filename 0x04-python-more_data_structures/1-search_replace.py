#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """search and replace an element in a list"""
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
