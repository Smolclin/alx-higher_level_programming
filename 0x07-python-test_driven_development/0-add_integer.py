#!/usr/bin/python3
'''Define a function that adds two integers'''


def add_integer(a, b=98):
    '''Returns the addition of integers a and b
    float arguements are type casted into ints before
    addition is performed
    Raises:
        TypeError: If neither a nor b is an integer nor a float'''
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
