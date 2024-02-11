#!/usr/bin/python3
'''Define function that devide matrix function'''


def matrix_divided(matrix, div):
    '''Divides all the elements of a matrix
    Args:
        matrix (list): A list of lists of intsor floats
        div (int/float): the divisor
    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if the matrix contains raws of different size
        TypeError: if div is not int or float
        ZeroDivisionError: if div is 0
    return:
        a new matrix representing division return'''
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elv, int) or isinstance(elv, float))
                    for elv in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
