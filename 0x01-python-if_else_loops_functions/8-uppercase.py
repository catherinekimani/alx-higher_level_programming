#!/usr/bin/python3
def uppercase(str):
    u = ""
    for idx in str:
        if ord(idx) >= 97 and ord(idx) <= 122:
            u = u + chr(ord(idx) - 32)
        else:
            u = u + idx
    print("{}".format(u))
