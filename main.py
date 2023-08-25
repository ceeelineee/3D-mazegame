from ursina import *
from player import *
from camera import *
from exit import *
from setup import *


def update(): 
    for wall in walls:
        wall.color = ground.color
        wall.texture = ground.texture

    for coin in coins:
        coin.animate_rotation((0, 5000, 0), duration = 1, loop = True)
        if coin.intersects(player).hit:
            player.coins += 1
            coins.remove(coin)
            destroy(coin)

    exitDoor.playerCollision()
        
def input(key):
    if key == 'q':
        exit()
    if key == 'b':
        ground.color = color.cyan
    if key == 'g':
        ground.color = color.green
    if key == 'r':
        ground.color = color.red
    if key == 'y':
        ground.color = color.white

    camera.input(key)

app = Ursina()
ground = Entity(
    model = 'plane',
    texture = 'sky_sunset',
    color = color.white,
    position = (WIDTH//2, 0, HEIGHT//2),
    scale = (WIDTH,1,HEIGHT),
    collider = 'mesh',
)
sky = Entity(
    model = 'cube',
    texture = 'assets\images\stars.png',
    # color = color.green,
    position = (WIDTH//2, 0, HEIGHT//2),
    scale = HEIGHT * 1.1,
    double_sided = True,
    collider = 'box'
)

start = Button(
    text = "Press 'P' to play",
    scale = BLOCKSIZE * 10,
    color = color.rgba(0, 0, 0, 150),
    highlight_color = color.rgba(0, 0, 0, 150),
    position = (0, 0, 0),
)

player = Player()
camera = Camera(player, start)

walls = [] 
coins = []
for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if MAP[i][j]:
            if MAP[i][j] == 'p':
                player.position = Vec3(BLOCKSIZE*i, 0, BLOCKSIZE*j)
                continue
            if MAP[i][j] == 'e':
                exitDoor = Exit(i, j, player)
                continue
            if MAP[i][j] == 'c':
                coin = Entity(
                    model = 'sphere',
                    texture = 'white_cube',
                    position = BLOCKPOSITION * Vec3(i, 1, j),
                    scale = COIN_SIZE * (1, 1, .2),
                    color = color.gold,
                    collider = 'sphere'
                )
                coins.append(coin)
                continue
            wall = Entity(
                model = 'cube',
                position = BLOCKPOSITION * Vec3(i, 1, j),
                scale = BLOCKSCALE,
                collider = 'box'
            )
            walls.append(wall)   
   
            
app.run()   