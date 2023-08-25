from ursina import *
from setup import *

class Coin(Entity):
    def __init__(self, x, y, player):
        super().__init__(
            model = 'circle',
            scale = COIN_SIZE,
            
        )
        