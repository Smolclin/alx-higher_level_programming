#!/usr/bin/python3
'''Define a class Student'''


class Student:
    '''epresents a student'''

    def __init__(self, first_name, last_name, age):
        '''initializes new student
        Args:
            first_name(str): the first name of the student
            last_name(str): the last name of the student
            age (int): the age of the student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''get the dictionary representation of the student'''
        return self.__dict__
