## Implementation of a Poker model for a planned application
## Model source: http://cowboyprogramming.com/2007/01/04/programming-poker-ai/


class Card:
    def __init__(self, value):
        self.value = 0

    def rank(self):
        return self.value%13

    def suit(self):
        return self.value/13

    def card(self):
        return self.value*13 + self.rank()




class Deck:
    def __init__(self, deck, discard):
        self.deck = []
        self.discard = []
        for i in range(0,52):
                self.deck.append() = Card(i)

    def shuffle(self):
        temp = self.deck
        for i in temp: # for the number of cards
            tin = randint(0,len(temp)) # choose a random index
            tca = temp[tin] # save card at aforementioned index
            temp[tin] = temp[i] # overwrite chosen card with card at i
            temp[i] = tca # overwrite ith card with save card
        self.deck = temp # overwrites original deck with shuffled temp

    def deal(self):
        return

    def draw(self):
        return self.deck.pop()
suit, rank
    def discard(self):
        self.discard.append(self.deck.pop())
        return

    def reset(self):
        return

class Game:
    def __init__(self, players, pot, deck):
        self.players = []
        self.pot = 0
        self.deck = Deck()
