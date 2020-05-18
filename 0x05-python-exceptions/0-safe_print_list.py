#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    if x == 0:
        print(x)
        return(x)
    try:
        for i in range(x):
            print(my_list[i], end="")
            c = c + 1
        print("")
        return(c)
    except IndexError:
        print("")
        return(c)
    except ValueError:
            pass
