#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxvalue = 0
    maxkey = None
    for i, j in a_dictionary.items():
        if j > maxvalue:
            maxvalue = j
            maxkey = i
    return maxkey
