#!/usr/bin/python3

'''task_01_duck_typing.py
Adding a class with abstract method and experimenting with the duck typing
method'''

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    '''Adding an abstract class'''
    @abstractmethod
    def area(self):
        '''abstract method to define the area of a shape'''
        pass

    @abstractmethod
    def perimeter(self):
        '''abstract method to define the area of a perimeter'''
        pass


def shape_info(shape):
    '''Print the shapes infos, using the duck typing technic'''
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


class Circle(Shape):
    '''Creating a subclass of Shape, Circle'''
    def __init__(self, radius):
        '''Initialization of the Circle'''
        self.radius = abs(radius)

    def area(self):
        '''Initialization of the area'''
        return pi * self.radius ** 2

    def perimeter(self):
        '''Initialization of the perimeter'''
        return pi * (self.radius * 2)


class Rectangle(Shape):
    '''Creating a subclass of Shape, Rectangle'''
    def __init__(self, width, height):
        '''Initialization of the rectangle'''
        self.width = width
        self.height = height

    def area(self):
        '''Initialization of the area'''
        return self.width * self.height

    def perimeter(self):
        '''Initialization of the perimeter'''
        return (2 * self.width) + (2 * self.height)
