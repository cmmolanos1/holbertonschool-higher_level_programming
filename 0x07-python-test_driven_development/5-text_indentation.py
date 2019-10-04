#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str or text is None or len(text) < 0:
        raise TypeError('text must be a string')

    t = list(text)

    for i in range(len(t)):
        if t[i] == '.' or t[i] == '?' or t[i] == ':':
            if i + 1 != len(t):
                if t[i + 1] == '.' or t[i + 1] == '?' or t[i + 1] == ':':
                    t.insert(i + 1, '\n\n')
                else:
                    t[i + 1] = '\n\n'
            else:
                t.insert(i + 1, '\n\n')

    text2 = "".join(t)
    print(text2, end='')
