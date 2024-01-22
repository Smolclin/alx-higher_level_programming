#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lenth = len(my_list)
    n_list = []
    for l in range(lenth):
        if my_list[l] % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return n_list
