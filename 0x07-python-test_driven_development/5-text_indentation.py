#!/usr/bin/python3
'''Define text printing function'''


def text_indentation(text):
    '''Define function that prints tex with
    two new lines after '.', '?' and ':'
    Args:
        text (str): the text to print
    raise:
        TypeError: if the text is not a string'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")

        if text[c] == '\n' or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
