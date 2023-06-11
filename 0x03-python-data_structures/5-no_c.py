#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    my_list = [s for s in my_list if s not in 'cC']
    new_str = ''.join(my_list)
    return new_str
