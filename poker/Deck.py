import Card

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



    def draw(self):
        return self.deck.pop()

    def discard(self):
        self.discard.append(self.deck.pop())
        return

    def reset(self):
        self.deck = Deck()
        self.deck.shuffle()
        return
