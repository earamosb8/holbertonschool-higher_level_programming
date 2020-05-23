#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test the function max_integer to get the max value"""

    def test_empty_list(self):
        """  an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_no_list(self):
        """ no list object"""
        self.assertEqual(max_integer('a'), 'a')
        self.assertEqual(max_integer("This is not a list"), 't')

    def test_with_floats(self):
        """floats"""
        my_test_list = [2.5, 3.2, 4.5, 4.8]
        self.assertEqual(max_integer(my_test_list), max(my_test_list))
        my_test_list = [0.5, 0.7, 0.8, 1.0]
        self.assertEqual(max_integer(my_test_list), max(my_test_list))
        my_test_list = [0.5, 0.55, 0.555, 0.6]
        self.assertEqual(max_integer(my_test_list), max(my_test_list))

    def test_with_ints(self):
        """ints positives"""
        my_test_list = [2, 3, 4, 40]
        self.assertEqual(max_integer(my_test_list), max(my_test_list))
        my_test_list = [5, 2, 5, 8]
        self.assertEqual(max_integer(my_test_list), max(my_test_list))

    def test_negative_ints(self):
        """ints negatives"""
        my_test_list = [-2, -3, 8, -40]
        self.assertEqual(max_integer(my_test_list), 8)
        my_test_list = [5, -2, -5, 10]
        self.assertEqual(max_integer(my_test_list), 10)
