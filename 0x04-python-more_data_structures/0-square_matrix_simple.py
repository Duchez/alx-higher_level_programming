#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Finds the square of all values in a matrix"""
    return ([[column * column for column in row] for row in matrix])
