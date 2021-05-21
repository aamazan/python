import Player
import Deck

class Game:
    def __init__(self, players, pot, deck):
        self.players = []
        self.pot = 0
        self.deck = Deck()

    def deal(self):
            for i in self.players:
                self.players[i].hand.append(self.deck.draw())
            for j in self.players:
                self.players[j].hand.append(self.deck.draw())
        return


# evalSeq takes a player's hand and returns whether it is a sequence or not and
#   the sequence if so
    def evalseq(): # TODO: figure out sequence algorithm
        # sort by rank
        # create three lists of subsets of cards to avoid nested loops
            # (groups 0-4, 1-5, 2-6)
        # set seq = false (0), counter = 0
        # while counter < 5
            # if hand[counter].rank == hand[counter + 1] + 1
            #   counter++
            # else break
        # if counter == 4
                # return seq = true, sequence group
        # else return seq = false, empty group
        return

    def evalsuit():
        # count number of same suit
        # if 5, flush, else not
        return

    def evalpairs():
        # base on number of cards of same rank
        # 2: one pair
        # 3: three of a kind
        # 4: two pair or four of a kind, check
        # 5: full house
        return

    def evalrank():
        # compare ranks of two hands until one has a higher high card
        # if full house, compare three of a kind rank before pair rank
        return

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
