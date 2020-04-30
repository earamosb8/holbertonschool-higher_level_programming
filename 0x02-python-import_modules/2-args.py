#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) > 1:
        cont = len(sys.argv)
        if cont == 2:
            print("{} argument:".format(cont - 1))
        elif cont > 1:
            print("{} arguments:".format(cont - 1))
        for x in range(1, cont):
            print("{}: {}".format(x, sys.argv[x]))
