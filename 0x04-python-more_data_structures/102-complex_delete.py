#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    rm_list = []
    for key, val in a_dictionary.items():
        if val == value:
            rm_list.append(key)
    for key in rm_list:
        a_dictionary.pop(key)
    return a_dictionary
