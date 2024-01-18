#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    summ = 0
    for j in range(1, len(argv)):
        summ += int(argv[j])
    print("{}".format(summ))
