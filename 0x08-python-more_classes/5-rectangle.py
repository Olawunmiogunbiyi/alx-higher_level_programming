#bin/usr/python3

#define rectangle attr
class Rectangle:
    """
    a class called a rectangle

    Args:
    width -of Rectangle
    height of Rectangle

    raise:

    TypeError if not int
    ValueError if value is less than zero
    """
    count_instances = 0

    def __init__ (self, width=0, height=0):
        #initiaize an instance of rectangle

        self.__width = width
        self.__height = height
        Rectangle.count_instances += 1

        @property
        def width(self):
            #return width rectangle
            return(self.__width)

            @width.setter
        def (width, value):
            """set attribute width"""
            if not isinstance (value,int):

                raise TypeError("width must be an interger")
                if value < 0
                raise ValueError("width must be >=0")

        self.__width = value

        @property
        def height(self):
            #return the height of a rectangle

            rturn (self.__height)

              @height.setter
    def height(self, value):
        """ sets the height of a rectangle """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ returns the area of a rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the perimeter of a rectangle """

        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ return a stirn representation of our object """

        if self.__width == 0 or self.__height == 0:
            return ""
        output = ['#' * self.__width for i in range(self.__height)]
        return "\n".join(output)

    def __repr__(self):
        """ to print a string representation of the object """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ to detect a deletion of an instance """
        print('Bye rectangle...')
        Rectangle.count_instances -= 1