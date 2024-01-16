#!/usr/bin/python3
for f_number in range(0, 10):
    for s_number in range(f_number + 1, 10):
        if f_number == 8 and s_number == 9:
            print("{}{}".format(f_number, s_number))
        else:
            print("{}{}, ".format(f_number, s_number), end='')
