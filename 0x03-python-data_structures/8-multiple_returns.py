#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        y = "None"
    else:
        y = sentence[0]
    x = len(sentence)
    tup = x, y
    return (tup)
