#!/usr/bin/env python3
def no_c(my_string):
    d = len(my_string)
    new_string = ""
    for i in range(d):
        if my_string[i] != 'C' and my_string[i] != 'c':
            new_string += my_string[i]
    return new_string
