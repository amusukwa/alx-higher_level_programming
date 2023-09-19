#!/usr/bin/python3
# test_square.py
"""
This module contains unit tests for the Square class in the models package.

It includes test cases for the constructor, attributes, methods, and other behaviors
of the Square class.
"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_constructor(self):
        # Test the constructor with size
        square1 = Square(5)
        self.assertEqual(square1.size, 5)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)
        self.assertEqual(square1.id, 17)

        # Test the constructor with size, x, and y
        square2 = Square(3, 2, 3)
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.x, 2)
        self.assertEqual(square2.y, 3)
        self.assertEqual(square2.id, 18)

        # Test the constructor with id, size, x, and y
        square3 = Square(4, 1, 1, 42)
        self.assertEqual(square3.size, 4)
        self.assertEqual(square3.x, 1)
        self.assertEqual(square3.y, 1)
        self.assertEqual(square3.id, 42)

    def test_size_property(self):
        square = Square(5)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_update_method(self):
        square = Square(5)
        square.update(10)
        self.assertEqual(square.id, 10)
        square.update(20, 8)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 8)
        square.update(30, 12, 3)
        self.assertEqual(square.id, 30)
        self.assertEqual(square.size, 12)
        self.assertEqual(square.x, 3)
        square.update(40, 15, 2, 5)
        self.assertEqual(square.id, 40)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 5)

    def test_update_method_with_args(self):
        square = Square(5)
        square.update(10)
        self.assertEqual(square.id, 10)

    def test_update_method_with_args(self):
        square = Square(5)
        square.update(size=10, x=2, y=3)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
 


if __name__ == '__main__':
    unittest.main()
