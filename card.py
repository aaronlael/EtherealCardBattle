import constants
from roll import roll
import random
import string

class Card:
    def __init__(self, deckid):
        self.id = self.cardid(deckid)
        self.statone = self.statbuild()
        self.stattwo = self.statbuild()
        while self.statone == self.stattwo and list(self.statone.keys())[0] in ['utility']:
            self.stattwo = self.statbuild()
        self.stats = self.statdict()
        self.cost = self.cardcost()

    def cardid(self, deckid):
        return deckid + ''.join(random.choices(string.hexdigits, k=4))

    def statbuild(self):
        stat = random.choice(constants.DECKVALS['types'])
        if stat in ['attack', 'proc']:
            return { stat : { random.choice(constants.DECKVALS[stat]) : roll('20') }}
        elif stat == 'utility':
            return { stat : { random.choice(constants.DECKVALS[stat]) : 1 }}
        else:
            return { stat : { random.choice(constants.DECKVALS[stat]): roll() }}


    def cardcost(self):
        ccost = 0
        if 'utility' in self.stats.keys():
            if len(self.stats['utility'].keys()) > 1:
                ccost += 10
            else:
                ccost += 5
        for key in [x for x in self.stats.keys() if x != 'utility']:
            for k in self.stats[key].keys():
                ccost += self.stats[key][k]
        return ccost


    def statdict(self):
        if list(self.statone.keys())[0] in self.stattwo.keys():
            k = list(self.statone.keys())[0]
            if list(self.statone[k].keys())[0] in list(self.stattwo[k].keys())[0]:
                k2 = list(self.statone[k].keys())[0]
                return { k : { k2 : self.statone[k][k2] + self.stattwo[k][k2] }}
            else:
                return { k : { **self.statone[k], **self.stattwo[k] }}
        else:
            return {**self.statone, **self.stattwo}
