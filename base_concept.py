import constants, card, deck, player
from roll import roll
import random
import string
import time

class Game():
    """main class for the actual game.  some portions will be turned into separate classes
    to make sure the main event loop of the game is manageable"""
    def __init__(self):
        self.id = self.gameid()
        self.players = []
        self.playspace = []
        self.deck = deck.Deck()
        self.turnindex = ''

    def gameid(self):
        """generate a 'unique' game id for future purpose"""
        return ''.join(random.choices(string.hexdigits, k=20))

    def addplayer(self, pname):
        """add a player class object to the game"""
        self.players += [player.Player(pname)]

    def theriver(self):
        """class method to present the current 8 cards during the build phase"""
        costlist, statonelist, stattwolist = [], [], []
        riverheader = [str(x) for x in range(1,9)]
        for card in self.playspace:
            costlist += [card.cost]
            statonelist += [list(card.statone.keys())[0]]
            stattwolist += [list(card.stattwo.keys())[0]]
        print('|' + '\t|'.join(riverheader).expandtabs(10))
        print('|cost ' + '\t|cost '.join([str(x) for x in costlist]).expandtabs(5))
        print('|' + '\t|'.join(statonelist).expandtabs(10))
        print('|' + '\t|'.join(stattwolist).expandtabs(10))


    def turntracker(self):
        """determines the first turn of the game, and keeps track of the turn turnindex
        function is called at the start of a game and at the end of a turn"""
        if self.turnindex == '':
            self.turnindex = random.choice(range(len(self.players)))
        else:
            if self.turnindex +1 == len(self.players):
                self.turnindex = 0
            else:
                self.turnindex += 1
        print(f"It looks like it's {self.players[self.turnindex].name}'s turn.")

    def turntaker(self, player):
        pass


    def start(self):
        print(constants.TITLE)
        input("Press any key to continue...")
        print("Let's add some players.  Type 'done' you're done!")
        while True:
            player = input("Enter a player name...")
            if player.lower() == 'done':
                break
            self.addplayer(player)
            print(f"{player} has entered the playspace...")
            print(f"The current players are { ', '.join([x.name for x in self.players])}")
        while len(self.playspace) < 8:
            self.playspace += [self.deck.deal()]

        if len(self.players) == 1:
            self.addplayer('_cpu_')
            self.players[-1].makecpu()
            print("Since you're playing solo, we'll add a _cpu_ opponent!")

        time.sleep(1)
        print("Let's see our first eight cards up for grabs!")
        self.theriver()
        self.turntracker()




if __name__ == '__main__':
    g = Game()
    g.start()
