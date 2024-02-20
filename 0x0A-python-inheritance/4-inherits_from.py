#!/usr/bin/python3
'''Define if the object is an instance of a class that inherited'''


def inherits_from(obj, a_class):
    '''a function that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from the specified
    class ; otherwise False
    Args:
        obj (any): the object to check
        a_class (type): the class to match the type of obj'''

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
