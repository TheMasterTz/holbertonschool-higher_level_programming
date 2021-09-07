#!/usr/bin/python3
for iter1 in range(100):
    if iter1 < 99:
        print('{:02}, '.format(iter1), end='')
    else:
        print(iter1)
