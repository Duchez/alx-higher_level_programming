#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    sums = 0
    for i in set(my_list):
        sums += i
    return result