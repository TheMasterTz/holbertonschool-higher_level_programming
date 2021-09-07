#!/usr/bin/python3
for iter1 in range(10):
    for iter2 in range(10):
        if (iter1 != iter2 and iter1 < iter2) and iter1 < 9:
            if iter1 == 8 and iter2 == 9:
                print('{}{}'.format(iter1, iter2))
            else:
                print('{}{}, '.format(iter1, iter2), end='')
