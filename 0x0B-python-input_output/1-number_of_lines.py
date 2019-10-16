#!/usr/bin/python3


def number_of_lines(filename=""):
    """Returns the numbers of lines in a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        count = 0
        for line in f:
            count += 1
    return count
