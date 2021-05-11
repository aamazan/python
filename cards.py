## Practice program for inheritance and other class-related topics

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number


class Deck:
    def __init__(self, deck):
        self.deck = []
        for i in range(1,5): # suits,
            for j in range(1,14):
                if i == 1:
                    suit = "spades"
                elif i == 2:
                    suit = "clubs"
                elif i == 3:
                    suit = "diamonds"
                else:
                    suit = "hearts"
                if j == 1:
                    num = "A"
                elif j > 1 and j < 11:
                    num = str(j)
                elif j == 11:
                    num = "J"
                elif j == 12:
                    num = "Q"
                else:
                    num = "K"
                self.deck.append() = Card(suit, num)

    def shuffle():
        return

    def deal():
        return

    def draw():
        return
