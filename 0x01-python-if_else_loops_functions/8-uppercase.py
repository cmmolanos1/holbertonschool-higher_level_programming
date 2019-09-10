#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        if 97 <= char <= 122:
            char = char -32
        if i == len(str) - 1:
            print(chr(char))
        else:
            print(chr(char), end = '')
            
            
