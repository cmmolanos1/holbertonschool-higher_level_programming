#!/usr/bin/python3
def no_c(my_string):
    s_list = list(my_string)
    i = 0
    while i < len(s_list):
        if s_list[i] == 'c' or s_list[i] == 'C':
            s_list.pop(i)
        else:
            i = i + 1
    new_str = "".join(s_list)
    return(new_str)
