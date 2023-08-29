#!/usr/bin/python3

class Square:
     """
    Class represents a square.

    Attributes:
        size (int):  Is size of the square.

    Methods:
        __init__(self, size=0):This Initializes a Square instance.
        area(self): Calculates and returns the area of the square.
        size(self): Getter method for size attribute.
        size(self, value): Setter method for size attribute.
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
        self.__size = size

    @property
    def size(self):
        """
        Getter method for size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: Is raised if size is not an integer.
            ValueError: Is raised if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
