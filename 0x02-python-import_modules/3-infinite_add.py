#!/usr/bin/python3
import sys

if __name__ == "__main__":
    len_args = len(sys.argv) - 1
    sum1 = 0

    if len_args > 1:
        for i in range(1, len_args):
            sum1 += int(sys.argv[i])
    print(sum1)
