#!/usr/bin/python3

"""Square module"""

class Square:
    """Class representing a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size

def main():
    """Main function to demonstrate Square class."""
    square = Square(5)
    print(square.__dict__)

if __name__ == "__main__":
    main()
