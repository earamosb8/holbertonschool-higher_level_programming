#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    " x_row : row of matrix "
    "cas : index of row"
    for x_row in matrix:
        for cas in x_row:
            if cas != x_row[len(x_row) - 1]:
                print("{:d}".format(cas), end=" ")
            else:
                print("{:d}".format(cas), end="")
        print("")
