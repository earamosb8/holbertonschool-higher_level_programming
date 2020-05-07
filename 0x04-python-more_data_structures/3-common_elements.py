#!/usr/bin/python3
def common_elements(set_1, set_2):
    tmp = []
    for i in set_1:
        for y in set_2:
            if i == y:
                if y not in tmp:
                    tmp.append(y)
    return(tmp)
