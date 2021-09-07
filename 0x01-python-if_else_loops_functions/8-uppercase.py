#!/usr/bin/python3
def uppercase(str):
    Newstr = ""
    for iter1 in range(len(str)):
        if (ord(str[iter1]) >= 97 and ord(str[iter1]) <= 122):
            Newstr += chr(ord(str[iter1]) - 32)
            continue
        Newstr += str[iter1]

    print('{0}'.format(Newstr))
