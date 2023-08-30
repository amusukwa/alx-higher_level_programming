#!/usr/bin/python3
"""This is shebang line"""

class Square:
    """ This represents a class square """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size

def main():
    """  Main function to show Square class."""
    square = Square(5)
    print(square.__dict__)

if __name__ == "__main__":
    main()
