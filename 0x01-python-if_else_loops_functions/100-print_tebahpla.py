#!/usr/bin/python3
for idx in range(122, 96, -1):
    if idx % 2 == 0:
        alph = idx
    else:
        alph = idx - 32
    print("{}".format(chr(alph)), end="")
