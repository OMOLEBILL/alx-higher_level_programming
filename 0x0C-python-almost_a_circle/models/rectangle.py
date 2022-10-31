#!/usr/bin/python3
"""We get the base class from the modules base
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """we initialize the the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width
        """
        return (self.__width)

    @width.setter
    def width(self, width):
        """ set the value of width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ return the value of height
        """
        return (self.__height)

    @height.setter
    def height(self, height):
        """ sets the value of height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ return the value of x
        """
        return (self.__x)

    @x.setter
    def x(self, x):
        """ sets the value of x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ returns the value of y
        """
        return (self.__y)

    @y.setter
    def y(self, y):
        """ sets the value for y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ return the area of the rectangle
        """
        return (self.width*self.height)

    def display(self):
        """ dispaly the class"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """prints the string of the class
        """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width,
                                                       self.height))

    def update(self, *args, **kwargs):
        """ adds the args
        """
        arg_list = ['id', '_Rectangle__width', '_Rectangle__height',
                    '_Rectangle__x', '_Rectangle__y']
        arg_dict = {'id': 'id', 'width': '_Rectangle__width',
                    'height': '_Rectangle__height',
                    'x': '_Rectangle__x', 'y': '_Rectangle__y'}
        for id, el in enumerate(args):
            self.__dict__[arg_list[id]] = el
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__dict__[arg_dict[key]] = val
