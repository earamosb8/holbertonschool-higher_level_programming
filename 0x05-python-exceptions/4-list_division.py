#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l1 = len(my_list_1)
    l2 = len(my_list_2)
    list_m = []
    for i in range(list_length):
        try:
            d = my_list_1[i] / my_list_2[i]
            list_m.append(d)
        except IndexError:
            print("out of range")
            list_m.append(0)
        except TypeError:
            print("wrong type")
            list_m.append(0)
        except ZeroDivisionError:
            print("division by 0")
            list_m.append(0)
    return(list_m)
