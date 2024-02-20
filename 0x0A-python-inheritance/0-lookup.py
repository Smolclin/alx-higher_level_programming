#!/usr/bin/python3
'''Define a function that returns the list of available attributes'''


def lookup(obj):
    '''returns the list of available attributes and methods of an object'''
    return dir(obj)
