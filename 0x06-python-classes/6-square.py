#!/usr/bin/python3
"""This is the shebang line"""


class Square:
    """
    Class represents a square.

    Attributes:
        size (int): size of a square.
        position (tuple): position of a square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a Square instance.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square with the character #.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: Is raised if size is not an integer.
            ValueError: Is raised if size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: Is raised if position is not a tuple or has less than 2 elements.
            ValueError: Is raised if elements of the tuple are not integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(element, int) and element >= 0 for element in value):
            raise ValueError("elements of position tuple must be positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

