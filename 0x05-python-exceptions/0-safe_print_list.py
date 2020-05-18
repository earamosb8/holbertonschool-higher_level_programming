#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    for elemento in my_list:
        cont += 1
    try:
        for i in range (0, x):
            print("{}".format(my_list[i]),end="")       
        return(i + 1)
    except IndexError:
        return(cont)
