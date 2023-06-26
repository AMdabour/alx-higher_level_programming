#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i, length = 0, 0
        for j in my_list:
            length += 1
        while i < x and i < length:
            print(f"{my_list[i]}", end='')
            i += 1
        print()
        return i
    except:
        pass
