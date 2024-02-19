#!/usr/bin/python3
'''Define LockedClass'''


class LockedClass:
    '''prevents the user from initiating new LockedClass attributes
    for anything but attributes called'''
    __slots__ = ["first_name"]
