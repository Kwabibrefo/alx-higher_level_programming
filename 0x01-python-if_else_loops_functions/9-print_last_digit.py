#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
        last_digit = -1 * (number % 10)
    else:
        last_digit = number % 10
    print("{}".format(last_digit))
