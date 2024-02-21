#!/usr/bin/python3
'''Define function that appends a string'''


def append_write(filename="", text=""):
    '''function that appends a string at the end of a text file (UTF8)
    Args:
        filename (str): the name of the file to be appended
        text (str): the string to append to the file'''

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
