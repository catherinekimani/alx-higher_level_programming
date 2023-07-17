#!/usr/bin/python3

""" Define a class name Base """
import json
import csv
import turtle


class Base:
    """ Base class for managing id attr in all future classes. """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for base
        Args:
            id (int): id value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string reoresentation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dicts_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dicts_list)
        with open(filename, mode='w', encoding='utf-8') as a_file:
            a_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list represented by json_string """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance of all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as a_file:
                dict_list = cls.from_json_string(a_file.read())
                instances = [cls.create(**d) for d in dict_list]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes and saves to a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as a_file:
            if list_objs is None or list_objs == []:
                a_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(a_file, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes and loads from a CSV file """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as a_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                rows = csv.DictReader(a_file, fieldnames=field_names)
                data = [dict((k, int(v)) for k, v in row.items())
                        for row in rows]
                return [cls.create(**d) for d in data]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window using the Turtle graphics module and
        draws all the rectangles and squares
        args:
            list_rectangles (list): list of rectangle objs
            list_squares (list): list of square objects
        """
        turtle_obj = turtle.Turtle()
        turtle_obj.screen.bgcolor("#B2EBF2")
        turtle_obj.pensize(3)
        turtle_obj.shape("turtle")

        turtle_obj.color("#ffffff")
        for rect in list_rectangles:
            turtle_obj.showturtle()
            turtle_obj.up()
            turtle_obj.goto(rect.x, rect.y)
            turtle_obj.down()
            for idx in range(2):
                turtle_obj.forward(rect.width)
                turtle_obj.left(90)
                turtle_obj.forward(rect.height)
                turtle_obj.left(90)
            turtle_obj.hideturtle()

        turtle_obj.color("#C3D9E8")
        for square in list_squares:
            turtle_obj.showturtle()
            turtle_obj.up()
            turtle_obj.goto(square.x, square.y)
            turtle_obj.down()
            for idx in range(2):
                turtle_obj.forward(square.width)
                turtle_obj.left(90)
                turtle_obj.forward(square.height)
                turtle_obj.left(90)
            turtle_obj.hideturtle()
        turtle.exitonclick()
