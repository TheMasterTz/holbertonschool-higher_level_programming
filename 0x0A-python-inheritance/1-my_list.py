#!/usr/bin/python3
"""
Contains the class MyList and list
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints a list in ascending order
        Sort a list and then prints on the output
        """

        if issubclass(MyList, list):
            print(sorted(self))
