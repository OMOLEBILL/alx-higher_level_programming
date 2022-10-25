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

    def to_json(self):
        """dict of class
        """
        return self.__dict__
