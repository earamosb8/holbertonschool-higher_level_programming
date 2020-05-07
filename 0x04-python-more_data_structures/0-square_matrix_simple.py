#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    l = []
    for x in matrix:
        l.append([j ** 2 for j in x])
    return(l)
