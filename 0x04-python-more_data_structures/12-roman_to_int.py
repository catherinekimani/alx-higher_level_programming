#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    res = 0
    prev = 0
    for char in reversed(roman_string):
        curr = roman_dict.get(char, 0)
        if curr >= prev:
            res += curr
        else:
            res -= curr
        prev = curr
    return res
