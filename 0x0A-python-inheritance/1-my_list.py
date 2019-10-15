#!/usr/bin/python3


class MyList(list):
    """Inherit from list"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
