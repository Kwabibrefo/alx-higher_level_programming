#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# store number % 10 as a variable called remainder
if number < 0:
    num = -1 * number
    remainder = -1 * (num % 10)
else:
    remainder = number % 10
# print Last digit of
print("Last digit of ", end="")
# print number
print("{} ".format(number), end="")
# print is
print("is ", end="")
# print remainder
print("{} ".format(remainder), end="")

if remainder > 5:
    print("and is greater than 5")
elif remainder == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
