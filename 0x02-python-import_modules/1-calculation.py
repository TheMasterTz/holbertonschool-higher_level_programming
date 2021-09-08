#!/usr/bin/python3
from __add__ import add
from __sub__ import sub
from __mul__ import mul
from __div__ import div

if __name__ == "__main__":
    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, add(a, b)))
    print('{} - {} = {}'.format(a, b, sub(a, b)))
    print('{} * {} = {}'.format(a, b, mul(a, b)))
    print('{} / {} = {}'.format(a, b, div(a, b)))
