# Author: Armaan Amazan
# Description: Prints n digits of e
import math

n = int(input())

print("Please enter how many digits of e you would like: ")

def digits(num):
    e = str(math.exp(1))
    if num == 1:
        return num
    else:
        num = e[:(num + 1)]
        return num

print(digits(n))

# TODO: implement rounding
