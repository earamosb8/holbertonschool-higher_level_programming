#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) > 1:
        cont = len(sys.argv)
        for x in range(1, cont):
            num = int(sys.argv[x])
            total = total + num
        print("{}".format(total))
        
