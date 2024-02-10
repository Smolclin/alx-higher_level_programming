#!/usr/bin/python3
'''Define  class square'''


class Square:
    '''represents a square'''
    def __init__(self, size=0):
        '''initializes new square
        Args:
            size (int): the size of the new square'''
        self.size = size

    @property
    def size(self):
        '''get the current size of the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return the area of the square'''
        return (self.__size * self.__size)

    def __eq__(self, other):
        '''define the == comparison to square'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''define the != comparison to square'''
        return self.area() != other.area()

    def __lt__(self, other):
        '''define the < comparison to square'''
        return self.area() < other.area()

    def __le__(self, other):
        '''define the <= comparison to square'''
        return self.area() <= other.area()

    def __gt__(self, other):
        '''define the > comparison to square'''
        return self.area() > other.area()

    def __ge__(self, other):
        '''define the >= comparison to square'''
        return self.area() >= other.area()
