from ursina import *
from setup import *

class Exit(Entity):
    def __init__(self, x, z, player):
        super().__init__(
            model = 'cube',
            collider = 'box'
        )
        self.color = color.magenta
        self.position = BLOCKPOSITION * Vec3(x, 1, z)
        self.scale = BLOCKSCALE
        self.player = player
        
    def update(self):
        self.playerCollision()
        
    def playerCollision(self):
        if self.intersects(self.player):
            self.color = color.yellow
            self.texture = 'radial_gradient'