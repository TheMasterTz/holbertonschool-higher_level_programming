#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last = number % 10
elif number < 0:
    last = ((number * -1) % 10) * -1

if last > 5:
    str = 'and is greater than 5'
elif last < 6:
    str = 'and is less than 6 and not 0'
else:
    str = 'and is 0'

print('Last digit of {} is {} {}'.format(number, last, str))
