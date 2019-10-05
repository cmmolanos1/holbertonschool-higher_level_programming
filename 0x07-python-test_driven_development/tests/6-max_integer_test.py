#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class to verify all edge cases in this function

    """
    def test_documentation(self):
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)

        self.assertTrue(len(max_integer.__doc__) > 0)

    def max_at_the_end(self):
        """ Biggest between positive number"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

if __name__ == '__main__':
    unittest.main()
