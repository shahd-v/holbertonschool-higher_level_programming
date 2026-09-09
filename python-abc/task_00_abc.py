#!/usr/bin/python3

'''task_00_abc.py
Module that use abstract class'''

from abc import ABC, abstractmethod


class Animal(ABC):
    '''Creating an abstract class'''
    @abstractmethod
    def sound(self):
        '''creating an abstract method'''
        pass


class Dog(Animal):
    '''Creating the subclass Dog'''
    def sound(self):
        '''Initialization of the abtsract method sound'''
        return "Bark"


class Cat(Animal):
    '''Creating the subclass Cat'''
    def sound(self):
        '''Initialization of the abtsract method sound'''
        return "Meow"
