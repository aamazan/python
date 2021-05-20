## Implementation of a Poker model for a planned application
## Model source: http://cowboyprogramming.com/2007/01/04/programming-poker-ai/

## notes to self for implementation:
# round counter, player status, side pots, player bet, database check for hands,
# hand calculation, probability of winning calculation, hand sorts (suit, rank)
#
# remember that hand calculation must take all combinations of the player's hand
# and the drawn cards and return the best of them
#
# player status check must include side-bets (player has gone all-in but others
# still have money for remaining rounds)
#
# as such, the game should have a global check to see if all active players have
# gone all-in, as well as when all players have been knocked payout
#
# include a case for hand comparison that splits pot between hands of equal value


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

    def discard(self):
        self.discard.append(self.deck.pop())
        return

    def reset(self):
        return

Class Player:
    def __init__(self, name, money, hand, betval, status):
        self.name = "Player"
        self.money = 5000
        self.hand = []
        self.betval = 0
        self.status = 0 # binary, where 1 is "folded" and 0 is still playing


class Game:
    def __init__(self, players, pot, deck):
        self.players = []
        self.pot = 0
        self.deck = Deck()


## game loop pseudocode
# initialize deck, set player order and blinds
# take blinds, deal cards (pop out of deck into hands in player order)
# "under the gun" begins blinds-betting round, iterate through players
# if bet, iterate through players until bet is matched, raised, or folded
#        (maybe at final player, check status of players/bets)
# once players are iterated through, deal and burn cards. start next round of bets.
#        need round counter, definitely need number of players/status check
# at end of round, if number of players >= 2 (remember to include side pots!)
#        showdown, calculate winning hand, payout
