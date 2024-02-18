#!/usr/bin/python3)
'''Define a class rectangle'''


class Rectangle:
    '''represents a rectangle
    attributes:
    number_of_instances (int): number of rectangle instances'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Initializes new a rectangle
        Args:
            width (int): the width of the rectangle
            heght (int): the height of the rectangle'''
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        '''get the width of the rectangle'''
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
        '''return the area of the rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height))

    def __str___(self):
        '''returns the printable representation of the rectangle
        represents the rectangle with # character'''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for j in range(self.__height):
            [rec.append('#') for k in range(self.__width)]
            if j != self.__height - 1:
                rec.append("\n")
        return "".join(rec)

    def __repr__(self):
        '''Return string representation of rectangle'''
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return rec

    def __del__(self):
        '''prints a message for deletion on the rectangle'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
