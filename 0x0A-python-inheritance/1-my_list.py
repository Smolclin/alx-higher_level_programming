#!/usr/bin/python3
''' a class MyList'''


class MyList(list):
    '''Define a class MyList that inherits from list'''

    def print_sorted(self):
        '''Public instance method that prints the list'''
        print(sorted(self))
