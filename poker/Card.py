#!/usr/bin/env python
"""The Card class defines the "card" object and its respective functions."""

class Card:
    def __init__(self, value):
        self.value = 0

    def rank(self):
        return self.value%13

    def suit(self):
        return self.value/13

    def card(self):
        return self.value*13 + self.rank()
