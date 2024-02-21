#!/usr/bin/python3
'''Define class Square that inherits from Rectangle'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''Represents the new square'''
    def __init__(self, size):
        '''Initializes a new square
        Args:
            size (int): the sze of the new square'''
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
