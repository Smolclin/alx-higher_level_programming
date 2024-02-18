#!/usr/bin/python3
'''Define a class Rectangle'''


class Rectangle:
    '''Represent a rectangle
    Attribures:
        number_of_instances (int): the number of rectangle instances
        print_symbol (any):the symbiol of rectangle representation'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''initializes a new rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle'''
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Returns the width of the rectangle'''
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
        '''Returns the height of the rectangle'''
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
        return self.__width * self.__height

    def perimeter(self):
        '''Returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''Returns the printable representation of the rectangle by #'''
        if self.__width == 0 or self.__height == 0:
            return ""

        rec = []
        for j in range(self.height):
            [rec.append(str(self.print_symbol))for k in range(self.__width)]
            if j != self.__height - 1:
                rec.append("\n")
        return "".join(rec)

    def __repr__(self):
        '''Return the string representation of rctangle'''
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        '''print every deletion done on the rectangle'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
