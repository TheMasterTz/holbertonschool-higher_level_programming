#!/usr/bin/python3
def fizzbuzz():
    n = 1
    while n < 101:
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz', end=' ')
        elif n % 3 == 0:
            print('Fizz', end=' ')
        elif n % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(n, end=' ')
        n += 1
