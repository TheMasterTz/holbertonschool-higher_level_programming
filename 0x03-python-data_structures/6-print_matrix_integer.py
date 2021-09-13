#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for element in matrix:
            i = 1
            length = len(element)
            for element in element:
                if i == length:
                    print("{:d}".format(element), end='')
                else:
                    print("{:d}".format(element), end=' ')
                i += 1
            print()
