#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    modified_list = []
    for idx in my_list:
        if idx % 2 == 0:
            modified_list.append(True)
        else:
            modified_list.append(False)
    return modified_list
