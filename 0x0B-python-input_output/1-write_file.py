#!/usr/bin/python3
'''Define function that writes a string to a text file'''


def write_file(filename="", text=""):
    '''Define function that writes a string to a text file
    (UTF8) and returns the number of characters written
    Args:
        filename (str): the file to write on
        text (str): the string to be written'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
