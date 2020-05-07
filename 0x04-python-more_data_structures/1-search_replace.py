#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = my_list[:]
    for i in range(len(my_list)):
        if n[i] == search:
            n[i] = replace
    return(n)
