#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Ldigit = abs(number) % 10

if Ldigit > 5:
    print(f"Last digit of {number} is {Ldigit} and is greater than 5")

elif Ldigit < 6 and Ldigit != 0:
    print(f"Last digit of {number} is {Ldigit} and is less than 6 and not 0")

elif Ldigit == 0:
    print(f"Last digit of {number} is {Ldigit} and is 0")
