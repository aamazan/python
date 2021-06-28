#!/usr/bin/env python
"""pancakesort.py is a solution attempt at a programming challenge (URL below)"""
# https://www.reddit.com/r/dailyprogrammer/comments/np3sio/20210531_challenge_392_intermediate_pancake_sort/

import math
import random


# returns index of largest element of an array
def largest(array):
    index = 0
    lgst = 0
    for i in range(0,len(array)):
        if array[i] > lgst:
            index = i
            lgst = array[i]
    return index

# returns the set with the subset indices up to the nth reversed
def flip_front(array, n):
    for i in range(0,math.floor(n/2)):
        temp = array[i]
        array[i] = array[(n-1)-i]
        array[(n-1)-i] = temp
    return array

# returns the set sorted from least to greatest (duplicate-inclusive)
def pancake_sort(array):
    for i in range(0, len(array)):
        l = largest(array[0:len(array)-i]) #largest in current subset
        flip_front(array, l+1)
        flip_front(array, len(array)-i)
    return array

# test cases (c is duplicate-inclusive case)
# a = [8,6,7,5,3,0,9]
# b = [2,1,13,1,5,8,3]
# c = []
# for i in range(0,10000):
#     c.append(random.randrange(0, 10000, 1))

# pancakesort(a)
# pancakesort(b)
# print(pancakesort(c))
