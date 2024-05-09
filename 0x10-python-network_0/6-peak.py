#!/usr/bin/python3
"""
Helps find peak in a list of unsorted integers
"""


def find_peak(list_integers):
    ''' finds the peak integer '''
    list_length = len(list_integers)
    end = list_length - 1
    if not list_integers:
        return None
    if list_integers[0] >= list_integers[1]:
        return list_integers[0]
    if list_integers[end] > list_integers[end - 1]:
        return list_integers[end]

    for nums in range(1, end):
        if list_integers[nums] > list_integers[nums + 1] and\
           list_integers[nums] > list_integers[nums - 1]:
            return list_integers[nums]
    return None
