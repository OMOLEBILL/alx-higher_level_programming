#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Ncheck = 0
if number < 0:
    number *= -1
    Ncheck = 1
digit = number % 10
if Ncheck == 1:
    number *= -1
    digit *= -1
print(f"Last digit of {number} is ", end="")
if digit > 5:
    print(f"{digit} and is greater than 5")
elif digit == 0:
    print(f"{digit} and is 0")
else:
    print(f"{digit} and is less than 6 and not 0")
