#!/usr/bin/python3
'''Define class Rectangle'''


class Rectangle:
    '''Represent rectangle'''
    def __init__(self, width=0, height=0):
        '''Initialize new rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''gets the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns the area of the rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''Returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        '''Return the printable representation of the rectangle
        represents the rectangle with the # character'''
        if self.__height == 0 or self.__height == 0:
            return ("")
        rec = []
        for j in range(self.__height):
            [rec.append("#") for k in range(self.__width)]
            if j != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))
