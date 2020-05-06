#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cas in row:
            print("{:d}".format(cas), end="")
            if cas != row[-1]:
                print(" ", end="")
        print(" ")
