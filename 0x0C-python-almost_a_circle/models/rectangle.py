#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width's getter"""
        return self.__width

    @property
    def height(self):
        """height's getter"""
        return self.__height

    @property
    def x(self):
        """x's getter"""
        return self.__x

    @property
    def y(self):
        """y's getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """Width's setter"""
        if type(value) is not int:
            raise TypeError("width must be and integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height's setter"""
        if type(value) is not int:
            raise TypeError("height must be and integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x's setter"""
        if type(value) is not int:
            raise TypeError("x must be and integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y's setter"""
        if type(value) is not int:
            raise TypeError("y must be and integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of rectangle"""
        return self.__width * self.__height
