#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    Mx = min(my_list)
    for i in my_list:
        if i > Mx:
            Mx = i
    return Mx
