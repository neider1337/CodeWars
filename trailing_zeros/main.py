import math

def zeros (x):
    i = 5
    zeros = 0
    while x >= i:
        zeros += x // i
        i *= 5
    return zeros