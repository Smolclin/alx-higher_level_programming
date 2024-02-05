#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nm = 0
    try:
        for item in range(x):
            print("{}".format(my_list[item]), end='')
            nm += 1
    except IndexError:
        pass
    print()
    return nm
