#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    ttal = 0
    number = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    for r in reversed(roman_string):
        number = digits[r]
        ttal += number if ttal < number * 5 else -number
    return ttal
