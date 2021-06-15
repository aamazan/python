#!/usr/bin/env python
"""pancakesort.py is a solution attempt at a programming challenge (URL listed in comments)"""
# https://www.reddit.com/r/dailyprogrammer/comments/np3sio/20210531_challenge_392_intermediate_pancake_sort/
import math


### PLEASE NOTE: This is currently unfinished, will post an accompanying
#                text file when complete


# returns index of largest element of an array
def largest(array):
    index = 0
    lgst = 0
    for i in range(0,len(array)):
        if array[i] >= lgst:
            index = i
            lgst = array[i]
    return index

# returns the set with the subset indices up to the nth reversed
def flipfront(array, n):
    for i in range(0,math.floor(n/2)):
        temp = array[i]
        array[i] = array[(n-1)-i]
        array[(n-1)-i] = temp
    return array

def pancakesort(array):
    sorted = 0 # number of elements sorted
    index = len(array)-1 # current "end" of unsorted subset
    print("sorted: "+ str(sorted))
    print("start index: "+ str(index))
    while sorted != len(array):
        if array[index] == largest(array[0:index+1]): # if current "end" is largest in unsorted
            sorted+=1
            index-=1
            print("sorted: "+ str(sorted))
            print("current index: "+ str(index))
            print("current largest: "+str(largest(array[0:index+1])))
        else:
            l = largest(array[0:index+1])
            flipfront(array, l) # flips largest to index 0
            print(array)
            flipfront(array, index+1) # flips largest to current "end"
            print(array)
            sorted+=1
            index-=1
            print("current largest: "+str(largest(array[0:index+1])))
            print("sorted: "+ str(sorted))
            print("current index: "+ str(index))
    return array

a = [6,7,2,1,5]

#print(a)
#print(pancakesort(a))
pancakesort(a)
# need to count back from largest array value through each iteration
# at what point is it sorted? let's find out

#count down from final index
#when it's the largest, find next largest of subset
