#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for idx in range(0, x):
            print("{}".format(my_list[idx]), end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
