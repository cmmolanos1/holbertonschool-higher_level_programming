#!/usr/bin/python3


def pascal_triangle(n):
    """Prints the n-pascal triangle"""
    lista = []
    if n <= 0:
        return lista
    for i in range(0, n):
        lista.append([1] * (i + 1))
        if i >= 2:
            for j in range(1, len(lista[i]) - 1):
                lista[i][j] = lista[i - 1][j] + lista[i - 1][j - 1]
    return lista
