#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return(1)
    elif b < 0:
        b = b * -1
        for y in range(1, b):
            a = a * a
            c = 1 / a
        return(c)
    elif a < 0:
        f = 1
        for d in range(1, b + 1):
            f = f * a
        return(f)
    else:
        f = 1
        for x in range(1, b + 1):
            f = f * a
        return(f)
