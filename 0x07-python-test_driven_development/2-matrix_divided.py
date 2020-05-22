#!/usr/bin/python3
"""This is the 0-add_integer module."""


def matrix_divided(matrix, div):
    mark = len(matrix[0])
    my_list = [[]]
    i = 0
    if isinstance(div, str) or i is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("ZeroDivisionError")
    for i in range(len(matrix)):
        for x in matrix[i]:
            if isinstance(matrix[i][x], str) or i is None:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                my_list[i][x].append(matrix[i][x] / div)
    return my_list 
                
   
    
    
