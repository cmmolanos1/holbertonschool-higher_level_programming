#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""
    count = 0
    with open(filename, 'r', encoding="utf-8") as f:
        if nb_lines > 0:
            for line in f:
                if count < nb_lines:
                    print(line, end='')
                    count += 1
                else:
                    break
        else:
            for line in f:
                print(line, end='')
