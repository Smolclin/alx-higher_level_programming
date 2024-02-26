#!/usr/bin/python3
'''define square clas'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''represent a square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initializes a new square
        Args:
            size (int): the size of the new square
            x (int): x coordinates of the new square
            y (int): y coordinates of the new square
            id (int): the identity of the new square'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''get the size of the square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''updates the square
        Args:
            *Args (int): new attribute values
            1st arguement represents id attribute
            2nd arguement represents size attribute
            3rd arguement represents x attribute
            4rth arguement represents y attribute
        **kwargs (dict): New key pair of attributes'''

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        '''returns the dictionary representation of the square'''
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}

        def __str__(self):
            '''returns the print() and str() representation of the square'''
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                     self.width)
