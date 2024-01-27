#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda f: replace if f == search else f, my_list))
