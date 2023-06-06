#!/usr/bin/python3
for idx1 in range(0, 10):
    for idx2 in range(idx1+1, 10):
        print("{:d}".format(idx1), end='')
        if idx1 == 8 and idx2 == 9:
            print("{:d}".format(idx2), end='\n')
        else:
            print("{:d}".format(idx2), end=', ')
