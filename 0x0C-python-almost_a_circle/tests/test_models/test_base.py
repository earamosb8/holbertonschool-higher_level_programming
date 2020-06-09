#!/usr/bin/python3

"""Unittest for Base class"""

import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Base tests"""

    def setUp(self):
        """setup of unittest"""
        Base._Base__nb_objects = 0

    def test_0(self):
        """Test number 0 for base"""
        b0 = Base()
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        b4 = Base(-1)
        self.assertEqual(b0.id, 1)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, -1)

    def test_1(self):
        """Test number 2 for base"""
        b0 = Base(id=None)
        self.assertEqual(b0.id, 1)

    def test_2(self):
        """Test number 1 for base"""
        b0 = Base("h")
        self.assertEqual(b0.id, "h")

    def test_3(self):
        """Test number 3 for base"""
        b0 = Base(0.03)
        self.assertEqual(b0.id, 0.03)

    def test_4(self):
        """Test number 4 for base"""
        b0 = Base(False)
        self.assertEqual(b0.id, False)

    def test_5(self):
        """Test number 5 for base"""
        b0 = Base(-16)
        self.assertEqual(b0.id, -16)

if __name__ == '__main__':
    unittest.main()
