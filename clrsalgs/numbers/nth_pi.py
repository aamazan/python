# Author: Armaan Amazan
# Description: Prints n digits of pi
import math

n = int(input())

print("Please enter how many digits of pi you would like: ")

def digits(num):
    p = str(math.pi)
    if num == 1:
        return num
    else:
        num = p[:(num + 1)]
        return num

print(digits(n))

# TODO: implement rounding
