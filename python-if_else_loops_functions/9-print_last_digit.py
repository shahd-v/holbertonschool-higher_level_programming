#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number) % 10
        number = -number
        return number
    else:
        number = number % 10
        return number
