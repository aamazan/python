#!/usr/bin/env python
"""chessboard.py is a solution attempt at a programming challenge (URL below)"""
# https://www.reddit.com/r/dailyprogrammer/comments/hrujc5/20200715_challenge_385_intermediate_the_almost/

# the flip function takes a series s of 64 bits and
# a number x s.t. 0 <= x <= 63
# input: 64-bit string, integer
# output: 64-bit string
def flip(s, flipnum):
    if s[flipnum] == "0":
        temp = list(s)
        temp[flipnum] = "1"
        s = "".join(temp)
    elif s[flipnum] == "1":
        temp = list(s)
        temp[flipnum] = "0"
        s = "".join(temp)
    return s


# check_board takes the current board and determines the encoded binary
# input: 64-bit string
# output: 6-bit string
def check_board(s):
    result = "000000"
    check = 0 # for determining number of heads per section
    resbit = 5 # current bit of result being checked for
    # columns: designated by %8 (e.g. 8%8 == 0%8 = 0, so same column)
    # every other  (1,3,5,7) ((0-7))
    for i in range(0,64):
        if i%8 == 1 or i%8 == 3 or i%8 == 5 or i%8 == 7:
            if s[i] == "1":
                check += 1
    checkres = str(check%2)
    temp = list(result)
    temp[resbit] = checkres
    result = "".join(temp)
    check = 0 # reinitialize
    resbit -= 1


    # skip two, check two (2,3,6,7)
    for i in range(0,64):
        if i%8 == 2 or i%8 == 3 or i%8 == 6 or i%8 == 7:
            if s[i] == "1":
                check += 1
    checkres = str(check%2)
    temp = list(result)
    temp[resbit] = checkres
    result = "".join(temp)
    check = 0
    resbit -= 1


    # check latter half (4,5,6,7)
    for i in range(0,64):
        if i%8 == 4 or i%8 == 5 or i%8 == 6 or i%8 == 7:
            if s[i] == "1":
                check += 1
    checkres = str(check%2)
    temp = list(result)
    temp[resbit] = checkres
    result = "".join(temp)
    check = 0
    resbit -= 1
    row = 0


    # rows:
    # every other  (1,3,5,7) ((0-7))
    for i in range(0,64):
        if row == 1 or row == 3 or row == 5 or row == 7:
            if s[i] == "1":
                check += 1
        if (i%8 == 7):
            row += 1
    checkres = str(check%2)
    temp = list(result)
    temp[resbit] = checkres
    result = "".join(temp)
    check = 0
    resbit -= 1
    row = 0


    # skip two, check two (2,3,6,7)
    for i in range(0,64):
        if row == 2 or row == 3 or row == 6 or row == 7:
            if s[i] == "1":
                check += 1
        if i%8 == 7:
            row += 1
    checkres = str(check%2)
    temp = list(result)
    temp[resbit] = checkres
    result = "".join(temp)
    check = 0
    resbit -= 1
    row = 0


    # check latter half (4,5,6,7)
    for i in range(0,64):
        if row == 4 or row == 5 or row == 6 or row == 7:
            if s[i] == "1":
                check += 1
        if i%8 == 7:
            row += 1
    checkres = str(check%2)
    temp = list(result)
    temp[resbit] = checkres
    result = "".join(temp)

    return result


# "Function prisoner1 takes two inputs: a series S of 64 bits,
# and a number X from 0 to 63 (inclusive).
# It returns a number Y from 0 to 63."
# input: 64-bit string, integer
# output: integer
def prisoner1(s,x):
    bits = '{0:06b}'.format(x) # get binary for x, outputs bitstring
    board = check_board(s) # board = current state bitstr
    tempbits = list(bits)
    tempboard = list(board)
    result = ""
    for i in range(0,6): # lazy xor implementation
        if tempbits[i] == tempboard[i]:
            result = result + "0"
        else:
            result = result + "1"
    result = int(result,2) # convert bitstr to int
    return result #square to be flipped


# "Function prisoner2 takes one input: a series T of 64 bits.
# It returns a number from 0 to 63."
# input: 64-bit string
# output: integer
def prisoner2(t):
    bits = check_board(t) # bitstr to decode
    result = int(bits,2) # convert bitstr to int
    return result


# Function solve provided with the prompt
def solve(S, X):
    Y = prisoner1(S, X)
    T = flip(S, Y)
    return prisoner2(T) == X


test = "1111100000011000011001010101001001001001111110011111010110000010"
test2 = "1011100100000111110000000100100010011000101000100100100110101111"

print(solve(test,5))
print(solve(test,58))
print(solve(test2,23))
print(solve(test2,11))
