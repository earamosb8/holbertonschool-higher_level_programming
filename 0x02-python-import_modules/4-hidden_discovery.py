#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    com = len(dir(hidden_4))
    res = dir(hidden_4)
    for x in range(0, com):
        f = res[x].find("__")
        if f == -1:
            print("{}".format(res[x]))
