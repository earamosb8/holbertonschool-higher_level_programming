#!/usr/bin/python 3
for x in range(0, 10):
    for y in range(0, 10):
        if x != 9 or y != 9:
            print("{}{}, ".format(x, y), end="")
        else:
            print("{}{}".format(x, y))
