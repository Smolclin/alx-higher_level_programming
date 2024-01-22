#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        first_string = my_string.translate({ord("c"): None})
        seco_string = first_string.translate({ord("C"): None})
        return seco_string
    return my_string
