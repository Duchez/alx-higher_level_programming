#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """multiply all values in a dictionary by 2"""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
