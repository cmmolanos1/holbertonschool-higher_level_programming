#!/usr/bin/python3
"""Class MagicClass"""
import math


class MagicClass:
    """Class to calculate circle area"""
    def __init__(self, radius=0):
        """Initializes the class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the circle's area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circle's circumference"""
        return 2 * math.pi * self.__radius
