#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    ListCart = ['?', '.', ':']

    iter1 = 0
    while iter1 < len(text):
        if text[iter1] in ListCart:
            print(text[iter1] + "\n")
            if iter1 + 1 == len(text):
                break
            iter1 += 1

            while text[iter1] == ' ':
                iter1 += 1
        else:
            print(text[iter1], end='')
            iter1 += 1

