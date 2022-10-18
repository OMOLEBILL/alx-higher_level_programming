#!/usr/bin/python3
""" defines an empty rectaangle
"""


class Rectangle():
    """Empty class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initililizes the class
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ return the value of size
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle
        """
        return (self.height * self.width)

    def perimeter(self):
        """ returns the perimeiter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * (self.height + self.width))

    def __str__(self):
        """Returns string
        """
        z = []
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                z.append(str(self.print_symbol) * self.__width)
            return ("\n".join(z))
        return ""

    def __repr__(self):
        """method: __repr__
           return : a nice string representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Method: __del__
            return: nothing
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ checking the biggest arrea
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
