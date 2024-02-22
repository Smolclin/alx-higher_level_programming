#!/usr/bin/python3
'''Define class Student'''


class Student:
    '''Represents student'''
    def __init__(self, first_name, last_name, age):
        '''a class Student that defines a student by:
        (based on 9-student.py)
        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Public method that retrieves a dictionary
        representation of a Student instance
        Args:
            attrs: the arrribute to represent'''

        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
