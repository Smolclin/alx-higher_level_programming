#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for l in sorted(a_dictionary.keys()):
        print("{}: {}".format(l, a_dictionary[l]))
