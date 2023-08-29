#!/usr/bin/python3

"""
Square module

The module defines a class
"""
class Square:
    """
    Class represents a square.

    Attributes:
        size (int): size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square instance.
        area(self): Computes and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: Is raised if size is not an integer.
            ValueError: Is raised if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        Calculteas area of the square.

        Returns:
            int:The area of a square.
        """
        return self.__size ** 2
