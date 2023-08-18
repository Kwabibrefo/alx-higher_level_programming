#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# store number % 10 as a variable called remainder
remainder = number % 10
# print Last digit of 
print("Last digit of ", end="")
# print number
print("{} ".format(number), end="")
# print is
print("is ", end="")
# print remainder
print("{} ".format(remainder), end="")

"""
use if elif to find if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
"""
if remainder > 5:
    print("and is greater than 5")
elif remainder == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

