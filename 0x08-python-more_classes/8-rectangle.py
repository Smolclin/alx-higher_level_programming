#!/usr/bin/python3
'''Defines a class Rectangle'''


class Rectangle:
    '''Represents rectangle

    Attributes:
        number_of_instance (int): the number of rectangle instances
        print_symbol (any): the symbol used for string representation'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''initializes the new rectangle
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
        '''Returns the hight of the rectangle'''
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
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the rectangle with greater area
        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle
        Raise:
            TypeError: if neither the first nor the second is a rectangle
            represent the rectangle with #'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        '''returns the printable representation of'''
        '''the rectangle with # character'''
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for j in range(self.__height):
            [rect.append(str(self.print_symbol)) for k in range(self.__width)]
            if j != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        '''Returns the string representation of rectangle'''
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        '''prints a message for the deletion that takes place'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
