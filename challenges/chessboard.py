#!/usr/bin/env python
"""chessboard.py is a solution attempt at a programming challenge (URL below)"""
# https://www.reddit.com/r/dailyprogrammer/comments/hrujc5/20200715_challenge_385_intermediate_the_almost/

# the flip function takes a series s of 64 bits and a
# a number x s.t. 0 <= x <= 63
def flip(s, flipnum):
    if s[flipnum] == 0:
        s[flipnum] = 1
    else:
        s[flipnum] = 0
    return s

# "Function prisoner1 takes two inputs: a series S of 64 bits,
# and a number X from 0 to 63 (inclusive).
# It returns a number Y from 0 to 63."
def prisoner1(s, x):
    # get binary for x
    # count heads in rows, columns to determine current encoding
    # figure out what to xor add to the current to get desired x binary

    # note: must interpret magic square as opposite value



    return

# "Function prisoner2 takes one input: a series T of 64 bits.
# It returns a number from 0 to 63."
def prisoner2(t):
    return

# Function solve provided with the prompt
def solve(S, X):
    Y = prisoner1(S, X)
    T = flip(S, Y)
    return prisoner2(T) == X

# check_board takes the current board and determines the encoded binary
def check_board(s):
    result = "000000"
    check = 0 # for determining number of heads per section
    resbit = 5 # current bit of result being checked for
    # columns: designated by %8 (e.g. 8%8 == 0%8 = 0, so same column)

    print(result)
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
        if (i%8 == 2) or (i%8 == 3) or (i%8 == 6) or (i%8 == 7):
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

test = "11111000000110000110010101010010010010011111100111110101100000100111111110101010"
print(check_board(test))
