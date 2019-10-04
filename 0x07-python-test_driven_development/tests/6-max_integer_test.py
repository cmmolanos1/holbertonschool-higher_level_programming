#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class to verify all edge cases in this function"""

    def negatives(self):
        """ Biggest between negatives number"""
        a = [-5, -100, -2, -1000]
        self.assertEqual(max_integer(a), -2)

    def positives(self):
        """ Biggest between positive number"""
        a = [5, 100, 2, 1000]
        self.assertEqual(max_integer(a), 1000)

    def both_posneg(self):
        """ Test mixing negatives and positives numbers"""
        a = [-2, -1, 0, 1, 2]
        self.assertEqual(max_integer(a), 2)

    def one_float(self):
        """ If one element is float"""
        a = [1, 2, 3.3, 4]
        self.assertEqual(max_integer(a), 4)

    def all_float(self):
        """ Teste when all elements are float"""
        a = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual(max_integer(a), 4.4)

    def all_same(self):
        """ Test when all elements are the same number"""
        a = [0, 0, 0, 0]
        self.assertEqual(max_integer(a), 0)

    def uniq_element(self):
        """ Test when there is only 1 element"""
        a = [0]
        self.assertEqual(max_integer(a), 0)

    def empty_list(self):
        """ Test if we input empty lists"""
        a = []
        self.assertIsNone(max_integer(a))

    def type_error(self):
        """ When is typed a non-float-int number"""
        a = [1, 2, "three", 4]
        with self.assertRaises(TypeError):
            max_integer(a)

    def none_case(self):
        """ None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def int_case(self):
        """ int as argument"""
        with self.assertRaises(TypeError):
            max_integer(0)

if __name__ == '__main__':
    unittest.main()
