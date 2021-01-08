#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix"""
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            print("{:d}".format(matrix[x][y]), end="")
            if y != (len(matrix[i]) - 1):
                print(" ", end="")

        print("")
