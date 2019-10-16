#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing
    a specific string"""
    str_file = ""
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            if search_string in line:
                str_file += line + new_string
            else:
                str_file += line

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(str_file)
