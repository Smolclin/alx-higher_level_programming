#!/usr/bin/python3
'''Define Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''represeent a rectangle using BaseGeometry'''
    def __init__(self, width, height):
        '''Initializes the rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle'''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''returns the area of the rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''returns the prisentable representation of the rectangle'''
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
