#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists) \
         of integers/floats')
    if type(div) != int:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    test = len(matrix[0])
    for row in matrix:
        if len(row) != test:
            raise TypeError('Each row of the matrix must have the same size')
    new = []
    for i in range(len(matrix)):
        new.append([])
    for j in range(len(matrix[i])):
        new[i].append(round(matrix[i][j] / div, 2))
    return new
