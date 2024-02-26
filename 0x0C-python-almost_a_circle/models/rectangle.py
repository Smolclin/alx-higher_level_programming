#!/usr/bin/python3
'''define a rectangle class'''
from models.sae import Base


class rectangle(Base):
    '''represents a rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializes a new rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the retangle
            x (int): x coordination of the rectangle
            y (int): y coordination of the rectangle
            id (int): the identity of the rectangle

        Raise:
            TypeError: if neither width nor height is an int
            ValueError: if either width or height is <= 0
            TypeError: if neither x nor y is an int
            ValueError: if either x or y is < 0'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''gets the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''get the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be  > 0")
        self.__height = value

    @property
    def x(self):
        '''gets the x coordinates of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''gets the y coordinates of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.height * self.width

    def display(self):
        '''prints the rectangle using the # character'''
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        '''updates the rectangle
        Args:
            *args: integer new pair attribute
                1st arguement represent id attribte
                2nd arguement represent width attribute
                3rd arguement represent height attribute
                4rth arguement represent x attribute
                5fth arguement represent y attribute
            **kwargs new pair value attributes'''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v, in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        '''returns the dictionary representation of rectangle'''
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        '''return the print() and string() representation of the rectangle'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
