#!/usr/bin/python3


class Base:
    """The Base class for managing object IDs.

    This class provides a base for managing object IDs. It keeps track of the number
    of objects created and assigns unique IDs to objects.

    Attributes:
        __nb_objects (int): A private class attribute that counts the number of objects
            created from this class.

    Methods:
        __init__(self, id=None): The constructor of the Base class. If an ID is provided,
            it assigns that ID to the object. Otherwise, it increments the __nb_objects
            count and assigns a unique ID to the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

