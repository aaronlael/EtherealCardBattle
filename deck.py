import card, constants
from roll import roll
import random
import string

class Deck():
    def __init__(self):
        self.id = self.deckid()
        self.cards = self.gencards(self.id)
        self.inplay = []
        self.discarded = []

    def gencards(self, deckid):
        cards = []
        for i in range(200):
            cards += [card.Card(deckid)]
        return cards

    def deckid(self):
        return ''.join(random.choices(string.hexdigits, k=4))

    def deal(self):
        c = self.cards[0]
        self.inplay += [c]
        self.cards = self.cards[1:]
        return c

    def discard(self, c):
        self.inplay.remove(c)
        self.discard += [c]

class Player():
    def __init__(self, pname='Player_1'):
        self.name = pname
        self.health = 60
        self.cards = []
        self.stats = self.basestats()
        self.currency = 0

    def basestats(self):
        stats = {}
        for type in constants.DECKVALS['types']:
            stats[type] = {}
            for stat in constants.DECKVALS[type]:
                stats[type][stat] = 0
        return stats

    def currencyadd(self, amt):
        self.currency += amt

    def currencyspend(self, amt):
        self.currency -= amt

    def receivecard(self, card):
        self.cards += [card]
        for key in card.stats.keys():
            for k in card.stats[key].keys():
                self.stats[key][k] += card.stats[key][k]
