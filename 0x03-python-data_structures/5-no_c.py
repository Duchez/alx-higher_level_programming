#!/usr/bin/python3
def no_c(my_string):
    """removes all c and C in a string"""
    duplicate = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(duplicate))
