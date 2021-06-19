#!/usr/bin/env python
""" Player.py defines the Player class and its associated functions."""
class Player:
    def __init__(self, name, money, hand, betval, status):
        self.name = "Player"
        self.money = 5000
        self.hand = []
        self.betval = 0
        self.status = 0 # binary, where 1 is "folded" and 0 is still playing

    def sortSuit(): # if same suit, sort by rank
        return

    def sortRank(): # if same rank, sort by suit (0-3)
        return
