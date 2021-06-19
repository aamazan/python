#!/usr/bin/env python
"""chessboard.py is a solution attempt at a programming challenge (URL below)"""
# https://www.reddit.com/r/dailyprogrammer/comments/hrujc5/20200715_challenge_385_intermediate_the_almost/

# the flip function takes a series s of 64 bits and a
# a number x s.t. 0<=x<=63
def flip(s, flipnum):
    if s[flipnum] == 0:
        s[flipnum] = 1
    else:
        s[flipnum] = 0
    return s

# "Function prisoner1 takes two inputs: a series S of 64 bits,
# and a number X from 0 to 63 (inclusive).
# It returns a number Y from 0 to 63.""
def prisoner1(s, x):
    return

# "Function prisoner2 takes one input: a series T of 64 bits.
# It returns a number from 0 to 63.""
def prisoner2(t):
    return

# Function solve provided with the prompt
def solve(S, X):
    Y = prisoner1(S, X)
    T = flip(S, Y)
    return prisoner2(T) == X
