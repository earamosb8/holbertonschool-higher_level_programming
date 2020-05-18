#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            c = c + 1
        except ValueError:
            pass
        except IndexError:
            pass
    print("")
    return(c)