#!/usr/bin/python3
def uniq_add(my_list=[]):
    tmp = []
    t = 0
    for i in my_list:
        if i not in tmp:
            tmp.append(i)
            t = t + i
    return(t)
