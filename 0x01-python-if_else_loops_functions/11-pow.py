#!/usr/bin/python3
def pow(a, b):
    f = 1
    if a < 0 and b < 0:
        b = b * -1
        for z in range(1, b + 1):
            f = f * a
            f = f * -1
            f = 1 / f
        return(f)
    elif b == 0:
        return(1)
    elif b < 0:
        b = b * -1
        for y in range(1, b):
            a = a * a
            c = 1 / a
        return(c)
    elif a < 0:
        for d in range(1, b + 1):
            f = f * a
        return(f)
    else:
        for x in range(1, b + 1):
            f = f * a
        return(f)
