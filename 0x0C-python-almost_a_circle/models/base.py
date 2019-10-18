#!/usr/bin/python3


class Base():
    """Base class of all other classes in this project
    The goal of it is to manage id attribute in all classes
    and to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
