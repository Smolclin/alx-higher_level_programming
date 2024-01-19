#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv
    arg_no = len(argv)
    if arg_no != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    i = int(argv[1])
    operator = argv[2]
    j = int(argv[3])
    if operator == '+':
        print("{} + {} = {}".format(i, j, add(i, j)))
    elif operator == '-':
        print("{} - {} = {}".format(i, j, sub(i, j)))
    elif operator == '*':
        print("{} * {} = {}".format(i, j, mul(i, j)))
    elif operator == '/':
        print("{} / {} = {}".format(i, j, div(i, j)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
