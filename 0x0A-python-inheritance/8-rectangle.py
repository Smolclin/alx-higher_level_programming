#!/usr/bin/python3
'''Defines class Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''represents a rectangle using BaseGeometry'''

    def __init__(self, width, height):
        '''initializes a rectangle
        Args:
            width (str): the width of the rectangle
            height (int): the height of the rectangle'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
