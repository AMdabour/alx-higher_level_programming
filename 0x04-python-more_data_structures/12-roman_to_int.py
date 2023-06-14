#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    if roman_string and type(roman_string) is str:
        romnum = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C', 100, 'D': 500, 'M': 1000}
        num = 0
        prev_value = 0
        for char in reversed(roman_string):
            value = romnum.get(char, 0)
            if value >= prev_value:
                num += value
            else:
                num -= value
            prev_value = value
        return num
    else:
        return 0
