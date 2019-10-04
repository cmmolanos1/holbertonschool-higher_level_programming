#!/usr/bin/python3

import numpy


def lazy_matrix_mul(m_a, m_b):

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for rows in m_a:
        if type(rows) is not list:
            raise TypeError('m_a must be a list of lists')
    for rows in m_b:
        if type(rows) is not list:
            raise TypeError('m_b must be a list of lists')

    if not m_a:
        raise ValueError('m_a can\'t be empty')
    if not m_b:
        raise ValueError('m_b can\'t be empty')

    for rows in m_a:
        for ele in rows:
            if type(ele) is not int and type(ele) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for rows in m_b:
        for ele in rows:
            if type(ele) is not int and type(ele) is not float:
                raise TypeError('m_b should contain only integers or floats')

    for rows in m_a:
        if len(rows) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for rows in m_b:
        if len(rows) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    m_a = numpy.array(m_a)
    m_b = numpy.array(m_b)

    return numpy.dot(m_a, m_b)
