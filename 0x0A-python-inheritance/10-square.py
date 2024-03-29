#!/usr/bin/python3
'''Define a class Square that inherits from Rectangle'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''represents a square'''
    def __init__(self, size):
        '''initializes a new square
        Args:
            size (int): the size of the square'''
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
