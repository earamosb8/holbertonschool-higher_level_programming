#!/usr/bin/python3
con = 0
for x in range(122, 96, -1):
    con = con + 1
    if con % 2 == 0:
        x = x - 32
        print("{}".format(chr(x)), end="")
    else:
        print("{}".format(chr(x)), end="")
