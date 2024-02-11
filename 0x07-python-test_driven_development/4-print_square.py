#!/usr/bin/python3
'''Define a square printing function with
character #'''


def print_square(size):
    '''prints a square with character #
    Args:
        size (int): the height and width of the square
    raise:
    TypeError if size is not integer
    ValueErro if value is < 0'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for m in range(size):
        [print("#", end="") for n in range(size)]
        print("")
