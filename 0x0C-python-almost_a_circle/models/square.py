#!/usr/bin/python3
"""
Class Square

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Print information about the Rectangle"""
        return "[Square] (" + str(self.id) + ") " + str(self.x) \
            + "/" + str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """size getters"""
        return self.width

    @size.setter
    def size(self, size):
        """setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updating the class reading variable arguments"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 4:
                self.x = args[2]
            if len(args) == 5:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['size'] = self.size
        dictionary['x'] = self.x
        dictionary['y'] = self.y

        return dictionary
