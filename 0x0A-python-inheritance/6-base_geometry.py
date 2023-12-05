#!/usr/bin/python3
""" area exception based on Geometry class """


class BaseGeometry:
    """ base class Geometry """

    def area(self):
        raise Exception("area() is not implemented")
