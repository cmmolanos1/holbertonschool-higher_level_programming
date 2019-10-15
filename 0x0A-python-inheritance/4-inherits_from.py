#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Defines if an object is if the object is an instance of
    a class that inherited (directly or indirectly) from the
    specified class"""
    return type(obj) != a_class and isinstance(obj, a_class)
