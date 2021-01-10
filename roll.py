import constants
import random

def roll(di='6'):
    return random.choice(constants.DI[di])
