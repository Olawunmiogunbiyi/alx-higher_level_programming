#!/usr/bin/python3
""" a function to print out a users name"""


def say_my_name(first_name, last_name=""):
    """ a function that prints full name

    Usage:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name(12, "White")
        Traceback (most recent call last):
        ...
        TypeError: first_name must be a string
        >>> say_my_name()
        Traceback (most recent call last):
        ...
        TypeError: say_my_name() missing 1 required positional argument: 'first_name'
    """

    if not isinstance(first_name, str) or first_name == None:
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
