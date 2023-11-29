#!/bin/usr/python3

#define rectangle

class Rectangle:
    def __init__(self, width=0, height=0):

        #private attribute for witdth
        self._width = 0

        #private attribute for witdth
        self._height = 0

        #set width  using the proper setter
        self.width = width

        #set height using the proper setter
        self.height = height

        @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
