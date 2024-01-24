#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = [row[:] for row in matrix]
    for idx, row in enumerate(n_matrix):
        for idx2, col in enumerate(n_matrix):
            n_matrix[idx][idx2] = row[idx2] ** 2
    return n_matrix
