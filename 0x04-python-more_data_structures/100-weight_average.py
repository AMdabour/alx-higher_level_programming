#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        num = 0
        bel = 0
        for tup in my_list:
            num += tup[0] * tup[1]
            bel += tup[1]
        return num / bel
    else:
        return 0
