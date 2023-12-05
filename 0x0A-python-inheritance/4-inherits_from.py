#!/usr/bin/python3
""" checks if a class is a subtype """


def inherits_from(obj, a_class):
    """ checks if an object is an instance of subclass """
    return True if issubclass(type(obj), a_class)\
        and type(obj) is not a_class else False
