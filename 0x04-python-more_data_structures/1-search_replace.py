#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #return [replace if i == search else i for i in my_list]
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
