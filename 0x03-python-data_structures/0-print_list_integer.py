#!/usr/bin/python3
def print_list_integer(my_list=[]):
    x = len(my_list)
    for y in range(0,x):
        print("{:d}".format(my_list[y]))
