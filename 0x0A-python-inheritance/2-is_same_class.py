#!/usr/bin/python3
'''Define if the object is exactly an instance'''


def is_same_class(obj, a_class):
    '''check if an object is an instance
    Args:
        obj (any): the object to check
        a_class (type): the class to match any object to be checked
    Return:
        if an object is an instance of a class - True
        otherwise - False'''

    if type(obj) is a_class:
        return True
    return False
