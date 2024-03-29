#!/usr/bin/python3
'''Define class square'''


class Square:
    '''represent square'''
    def __init__(self, size=0, position=(0, 0)):
        '''initialize new square
        Args:
            size (int): size of the new square
            position (int, int): position of the new square'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Get the current size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Get the current position of the square'''
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        '''returns the area of the square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''print the square with the # character'''
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        '''Define print representation of a square'''
        if self.__size == 0:
            return ""

        result = ""
        result += '\n' * self.__position[1]

        for i in range(self.__size):
            result += ' ' * self.__position[0]
            result += '#' * self.__size
            if i < self.__size - 1:
                result += '\n'

        return result
