#!/usr/bin/python3
import ramdom
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
if digit > 5:
    print("greater that 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and 0")
