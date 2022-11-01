#!/usr/bin/python3
"""base class
"""


class Base():
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list dictionaries."""
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(self, list_objs):
        """Write the JSON representation to a file."""
        a = []
        for i in list_objs:
            a.append(self.to_json_string(i.__dict__))
        name = list_objs[0].__class__.__name__ + ".json"
        with open(name, 'w', encoding="utf-8") as f:
            json.dump(a, f)

    def from_json_string(json_string):
        """Returns a list of JSON representation."""
        return (json.loads(json_string))

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        """Cretaes an instance using a dictionary."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            i = Rectangle(1, 2)
        elif cls is Square:
            i = Square(1)
        else:
            i = None
        i.update(**dictionary)
        return i

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves object to csv file."""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[i.id, i.width, i.height, i.x, i.y]
                             for i in list_objs]
            else:
                list_objs = [[i.id, i.size, i.x, i.y]
                             for i in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Loads object to csv file."""
        from models.rectangle import Rectangle
        from models.square import Square
        file_n = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for i in reader:
                i = [int(r) for r in row]
                if cls is Rectangle:
                    dct = {"id": i[0], "width": i[1], "height": i[2],
                           "x": i[3], "y": i[4]}
                else:
                    dct = {"id": i[0], "size": i[1],
                           "x": i[2], "y": i[3]}
                file_n.append(cls.create(**dct))
        return file_n

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            a = turtle.Turtle()
            a.color((randrange(255), randrange(255), randrange(255)))
            a.pensize(1)
            a.penup()
            a.pendown()
            a.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            a.pensize(10)
            a.forward(i.width)
            a.left(90)
            a.forward(i.height)
            a.left(90)
            a.forward(i.width)
            a.left(90)
            a.forward(i.height)
            a.left(90)
            a.end_fill()

        time.sleep(5)
