#!/usr/bin/python3
'''define class square'''


class Square:
    '''represent square'''
    def __init__(self, size=0):
        '''intitalize a new square
        args:
        size(int): size of the new square'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
