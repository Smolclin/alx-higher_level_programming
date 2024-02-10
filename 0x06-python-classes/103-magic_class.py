#!/usr/bin/python3
'''define MagicClass that does exactly the same as
the following Python bytecode'''

import math


class MagicClass:
    '''represent a circle'''
    def __init__(self, radius=0):
        '''initialize a magic class
        Args:
            radius (int, float): the radius of the new MagicClass'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''returns the area of MagicClass'''
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        '''returns the circumfere of MagicClass'''
        return (2 * math.pi * self.__radius)
