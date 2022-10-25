#!/usr/bin/python3
"""class student
"""


class Student():
    """class student
    """
    def __init__(self, first_name, last_name, age):
        """instanciate the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict of class
        """
        z = {}
        if type(attrs) is list and all(type(x) for x in attrs):
            for i in attrs:
                if i in self.__dict__:
                    z.update({i: self.__dict__[i]})
            return z
        return self.__dict__
