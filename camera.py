from ursina import *
from setup import *

class Camera(EditorCamera):
    def __init__(self, player, start):
        super().__init__(
            position = (WIDTH//2, HEIGHT//2, HEIGHT//2),
            rotation = (90, 0, 0)
        )
        self.music = Audio('/assets/audio/alienSoundTrack(1).mp3', volume = 1, loop = True)
        self.enabled = True
        self.player = player
        self.start = start
    
    def input(self, key):
        #camera and player view toggle
        if key == 'e':
            self.start.visible = True
            self.enabled = True
            self.position = self.player.position + Vec3(0, HEIGHT//2, 0)
            self.player.enabled = False
        if key == 'p':
            self.music.volume = 1
            self.start.text = "Press 'P' to continue"
            self.start.color = color.rgba(0, 0, 0, 0)
            self.start.visible = False
            self.enabled = False
            self.player.enabled = True
