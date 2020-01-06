#!/usr/bin/python3
""" Find peak """


def peak(lista, i, j, n):
    """ Divide and conquer """
    m = i + (j - i)//2

    if ((m == 0 or lista[m - 1] <= lista[m]) and
            (m == n - 1 or lista[m + 1] <= lista[m])):
        return lista[m]
    elif (m > 0 and lista[m - 1] > lista[m]):
        return peak(lista, i, m - 1, n)
    else:
        return peak(lista, m + 1, j, n)


def find_peak(list_of_integers):
    """ Find peak """
    if not list_of_integers:
        return
    n = len(list_of_integers)
    return peak(list_of_integers, 0, n - 1, n)
