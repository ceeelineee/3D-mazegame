from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from setup import BLOCKHEIGHT, HEIGHT

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            model="cube",
            jump_height= BLOCKHEIGHT,
            jump_duration= 3,
            origin_y=-2,
            collider="box",
            speed=10
        )
        self.cursor.color = color.rgba(0, 0, 0, 0)
        self.coins = 0
        self.pos = Text(
            text = f'   x: {int(self.x)}   |   z: {int(self.z)}   ',
            origin = (0, 0),
            color = color.rgba(255, 255, 255, 200),
            visible = False
        )
        self.speedText = Text(
                origin = (7, -18.5),
                color = color.rgba(255, 255, 255, 100)
            )
        self.coinsText = Text(
                origin = (-7, -18.5),
                color = color.rgba(255, 255, 255, 100)
            )
        self.showCoor = False
      

    def update(self):
        super().update()
        self.pos.text = f'   x: {int(self.x)}   |   z: {int(self.z)}   '
        self.speedText.text = f'Speed: {self.speed}'
        self.coinsText.text = f'Coins: {self.coins}'
        
    def input(self, key):
        super().input(key)
        if key == '1':
            self.speed = 20
        if key == '0':
            self.speed = 10
        if key == 'f3':
            self.showCoor = not self.showCoor
            if self.showCoor:
                self.pos.visible = True
            else:
                self.pos.visible = False