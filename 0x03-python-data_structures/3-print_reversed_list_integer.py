#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return (None)
    my_list.reverse()
    for list in my_list:
        print("{:d}".format(list))
