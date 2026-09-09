#!/usr/bin/python3
'''task_04_flyingfish.py
Module that add the classes fish and bird and a subclass of both'''


class Fish():
    # Creating a parent class fish

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird():
    # Creating a parent class bird

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    # Creating a subclass with multiple inheritance and modifying their methods
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
