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
        """delete existing files"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_00(self):
        """Test - checking attributes"""
        s1 = Rectangle(4, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s2 = Rectangle(3, 4, 5)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 4)
        self.assertEqual(s2.x, 5)
        self.assertEqual(s2.y, 0)

    def test_01(self):
        """check if is integer value"""
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(None, 3)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle((2, ), 3)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s2 = Rectangle("x", 5)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s2 = Rectangle(4.5, 6)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle([2, 3], 4)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(2, "x")
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(5, None)
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(4, (5, ))
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(5, [4, 3])
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s2 = Rectangle(5, 7.6)
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(1, 2, "s")
        self.assertEqual(
            "x must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(1, 3, 5.6)
        self.assertEqual(
            "x must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(2, 4, 4, "g")
        self.assertEqual(
            "y must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(2, 4, 5, 5.6)
        self.assertEqual(
            "y must be an integer",
            str(err.exception))
        s1 = Rectangle(5, 4, 3, 2, "s")
        self.assertEqual(s1.id, "s")
        s2 = Rectangle(5, 4, 3, 2, False)
        self.assertEqual(s2.id, False)
