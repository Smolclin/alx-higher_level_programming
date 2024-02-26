#!/usr/bin/python3
'''Defines base model class'''
import json
import csv
import turtle


class Base:
    '''Introduces new class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def ti_json_string(list_dictionaries):
        '''Returns the JSON serialization of a list dictionaries
        Args:
            list_dictionaries (list): list of dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Write the JSON serialization of a list of objs to a file
        Args:
            list_objs (list): list of inherited instances'''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''returns deserialization of JSON string
        Args:
            json_string (str): a JSON string representation of list
            return:
                if json_string is None or empty - an empty list
                otherwise - the python list is rep by json_string'''

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''return class instantied from a dictionary of attributes
        Args:
            **dictionary (dict): Value pair to initialize'''
        if dictionary and dictionary == {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        '''return a list od classes instanciated from JSON string
        reads from '<cls.__name__>.json'
        Return:
            if the file does not exist - an empty file
            otherwise - list of instanciated classes'''
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''write the CSV serialization of a list of objects to a file
        Args:
            list_objs (list): a list of inherited base instances'''
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs is []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                write = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Returns a listof files instanciated from csv file
        reads from '<cls.__name__>.csv'
        return:
        if the file does not exist - empty list
        othewise - list of instanciated classes'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    filename = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''draws rectangles and squares using the turtle module
        Args:
            list_rectangles (list): list of rectangle objects to draw
            list_squares (list): list of square objects to draw'''
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

            turt.color("#b5e3d8")
            for sq in list_squares:
                turt.showturtle()
                turt.up()
                turt.goto(sq.x, sq.y)
                turt.down()
                for i in range(2):
                    turt.forward(sq.width)
                    turt.left(90)
                    turt.forward(sq.height)
                    turt.left(90)
                turt.hideturtle()

            turtle.exitonclick()
