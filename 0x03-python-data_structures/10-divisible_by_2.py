#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Newlist = []
    for i in my_list:
        if i % 2 == 0:
            Newlist.append(True)
        else:
            Newlist.append(False)
    return Newlist
