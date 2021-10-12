#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')

read_file("my_file_0.txt")
