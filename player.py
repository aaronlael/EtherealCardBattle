import constants

class Player():
    def __init__(self, pname='Player_1'):
        self.cpu = False
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

    def makecpu(self):
        self.cpu = True

    def currencyadd(self, amt):
        self.currency += amt

    def currencyspend(self, amt):
        self.currency -= amt

    def receivecard(self, card):
        self.cards += [card]
        for key in card.stats.keys():
            for k in card.stats[key].keys():
                self.stats[key][k] += card.stats[key][k]
