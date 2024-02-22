#!/usr/bin/python3
'''class Student'''


class Student:
    '''represents student'''
    def __init__(self, first_name, last_name, age):
        '''initializes new student
        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''The dictionary representation of the student
        Args:
            attrs (list): the attributes to represent'''
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        '''replace all attributes all the student's attribute
        Args:
            json (dict): the value pair to replace attribute with'''
        for k, v in json.items():
            setattr(self, k, v)
