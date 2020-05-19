#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_m = []
    for i in range(list_length):
        try:
            d = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            list_m.append(d)
    return(list_m)
