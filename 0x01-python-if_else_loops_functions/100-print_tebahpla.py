#!/usr/bin/python3
for j in range(ord('z'), ord('a') - 1, - 2):
    print("{}{}".format(chr(j), chr(j - 33)), end='')
