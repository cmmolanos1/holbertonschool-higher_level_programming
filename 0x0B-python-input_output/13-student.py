#!/usr/bin/python3


class Student():
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        json_dict = {}

        for key2 in attrs:
            try:
                if self.__dict__[key2]:
                    json_dict[key2] = self.__dict__[key2]
            except:
                pass

        return json_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
