#!/usr/bin/python3
def roman_to_int(s):

    if type(s) is str:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            if i > 0 and rom[s[i]] > rom[s[i - 1]]:
                num += rom[s[i]] - 2 * rom[s[i - 1]]
            else:
                num += rom[s[i]]
        return num
    else:
        return 0
