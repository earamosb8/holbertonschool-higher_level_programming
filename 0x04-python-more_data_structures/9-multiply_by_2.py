#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = {}
    for x in a_dictionary:
        dic[x] = a_dictionary[x] * 2
    return(dic)
