#!/usr/bin/python3
"""
Unittests - Rectangle class
"""

import contextlib
import io
import unittest
import sys
import os
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Rectangle test"""

    def setUp(self):
        """setup of unittes"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """delete files"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_0(self):
        """checking attributes"""
        s1 = Rectangle(5, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s2 = Rectangle(3, 4, 5)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 4)
        self.assertEqual(s2.x, 5)
        self.assertEqual(s2.y, 0)
