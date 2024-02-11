#!/usr/bin/python3
'''Define a function that prints name'''


def say_my_name(first_name, last_name=""):
    '''print name
    Args:
        first_name (str): the first name to print
        last_name (str): the last name to print
    raise:
        TypeError: if neither first_name nor last_name
        is a string'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
