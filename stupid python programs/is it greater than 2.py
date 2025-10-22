import time

number = input("enter value:")
try:
    number = float(number)
except ValueError:
    print("did you really think that was a number?")
    exit()
if number > 2:
    print(number, "is bigger than two")
if number < 2:
    print(number, "is smaller than two")
if number == 2:
    print(number, "is equal to two")
