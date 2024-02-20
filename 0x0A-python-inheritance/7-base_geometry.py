#!/usr/bin/python3
'''Define a class BaseGeometry (based on 6-base_geometry.py)'''


class BaseGeometry:
    '''Represents class BaseGeometry'''

    def area(self):
        '''not yet implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates parameter as value
         Args:
            name (str): the name of the parameter
            value (int): the value to validate

        Raise:
            TypeError: if the value is not an integer
            ValueError: if the value <= 0'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
