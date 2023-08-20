#!/usr/bin/python3
def uppercase(alph):
    for i in alph:
        i = ord(i)
        if (i >= 97) and (i <= 122):
            i -= 32
        print("{:c}".format(i), end="")
    print("")
