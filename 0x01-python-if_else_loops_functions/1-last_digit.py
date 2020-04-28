#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
copy = number
if number < 0:
    number = number * -1
last = number % 10
print("Last digit of {} is {} ".format(copy, last), end="")
if last > 5:
    print("and is greater than 5".format(copy, last))
elif last == 0:
    print("and is 0".format(copy, last))
elif last < 6 and last != 0:
    print("and is less than 6 and not 0".format(copy, last))
