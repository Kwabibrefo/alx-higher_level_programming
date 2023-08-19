#!/usr/bin/python3
def uppercase(alph):
    for i in ord(alph):
        if (i >=97) and (i <= 122):
            i -= 32
            print("{:c}".format(i), end="")
        else:
            print(i)
