#!/usr/bin/python3
import sys

if __name__ == "__main__":
    len_args = len(sys.argv) - 1

    if len_args > 1:
        print(len_args, "arguments:")
        for i in range(1, len_args + 1):
            print('{}: {}'.format(i, sys.argv[i]))
    elif len_args == 1:
        print(len_args, "arguments:")
        for i in range(1, len_args + 1):
            print('{}: {}'.format(i, sys.argv[i]))
    elif len_args == 0:
        print(len_args, "arguments.")
