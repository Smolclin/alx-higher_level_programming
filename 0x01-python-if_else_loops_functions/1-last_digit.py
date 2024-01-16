#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -(lastdigit)
thestring = f"Last digit of {number} is {lastdigit}"
if lastdigit > 5:
    print(f"{thestring} and is greater than 5")
elif lastdigit == 0:
    print("{} and is 0".format(thestring))
elif lastdigit < 6:
    print("{} and is less than 6 and not 0".format(thestring))
