## Practice program for inheritance and other class-related topics


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number


class Deck:
    def __init__(self, deck, discard):
        self.deck = []
        self.discard = []
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

    def shuffle(self):
        temp = self.deck
        for i in temp:
            tin = randint(0,len(temp)) #  temporary index
            tca = temp[tin] # save random card
            temp[tin] = temp[i] # set aforementioned random card to card at i
            temp[i] = tca # set cart at i to original random card
        self.deck = temp

    def deal(self):
        return

    def draw(self):
        return self.deck.pop()

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
