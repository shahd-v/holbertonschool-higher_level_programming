#!/usr/bin/python3
'''task_05_dragon.py
Module that add two mixin methods to a class'''


class SwimMixin():
    # First mixin
    def swim(self):
        print("The creature swims!")


class FlyMixin():
    # Second mixin
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    # Class that inherite from two mixins
    def roar(self):
        print("The dragon roars!")
