#!/usr/bin/python3
'''Defie if the object is an instance'''


def is_kind_of_class(obj, a_class):
    '''a function that returns True if the object is an instance
    of, or if the object
    is an instance of a class that inherited
    from, the specified class ; otherwise False
    Args :
    obj any): the object to check'''

    if isinstance(obj, a_class):
        return True
    return False
