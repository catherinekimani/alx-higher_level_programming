#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mykeys = sorted(a_dictionary.keys())
    for key in mykeys:
        print(f"{key}: {a_dictionary[key]}")
