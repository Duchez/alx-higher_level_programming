#!/usr/bin/python3

def best_score(a_dictionary):
    scs = list(a_dictionary.keys())[0]
    biggest = a_dictionary[scs]
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            scs = key
    return scs
