#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        list_values = list(a_dictionary.values())
        list_keys = list(a_dictionary.keys())
        return list_keys[list_values.index(max(list_values))]
    else:
        return None
