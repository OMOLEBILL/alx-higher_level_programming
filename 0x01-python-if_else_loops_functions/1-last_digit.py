#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strnum = str(number)
if int(strnum[-1]) > 5:
     print("last digit of " + strnum + " is " + strnum[-1] + " and is greater than 5")
elif int(strnum[-1]) == 0:
    print("last digit of " + strnum + " is " + strnum[-1] + " and is 0")
elif int(strnum[-1]) < 6 and int(strnum[-1]) != 0:
     print("last digit of " + strnum + " is " + strnum[-1] + " and is less than 6 and not 0")
