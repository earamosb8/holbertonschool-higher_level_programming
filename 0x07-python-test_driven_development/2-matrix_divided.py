#!/usr/bin/python3
"""This is the 0-add_integer module."""


def matrix_divided(matrix, div):
    """this functions divided a matrix, Return New matrix"""

    my_matrix = [i[:] for i in matrix]
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists)\
     of integers/floats")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if isinstance(div, str) is True:
        raise TypeError('div must be a number')
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if isinstance(matrix[x][y], (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists)\
     of integers/floats")
    for i in range(0, len(matrix)):
        if (len(matrix[0]) != len(matrix[i])):
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(0, len(my_matrix)):
            for j in range(0, len(my_matrix[0])):
                my_matrix[i][j] = round(my_matrix[i][j] / div, 2)
    return(my_matrix)
