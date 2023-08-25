from ursina import *

# world
_ = False
BLOCKSIZE = 5
BLOCKHEIGHT = BLOCKSIZE * 1.1
BLOCKSCALE = (BLOCKSIZE, BLOCKHEIGHT, BLOCKSIZE)
BLOCKPOSITION = (BLOCKSIZE, 1, BLOCKSIZE)

COIN_SIZE = 1


MAP = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 'e', 20],
    [1, _, 3, _, _, 6, 7, _, 9, 10, _, 12, _, _, 15, _, 17, _, 19, 20],
    [1, _, _, _, 5, 6, 7, _, 9, _, _, 12, _, 14, 15, _, 17, 18, _, 20],
    [1, _, 3, 'c', _, _, 7, _, 9, 10, _, _, _, _, 15, _, _, _, _, 20],
    [1, _, _, 4, _, 6, _, 8, _, _, _, 12, _, 14, 15, _, 17, 18, 19, 20],
    [1, _, 3, 4, _, _, 'c', _, _, 10, 11, _, 13, _, 15, _, _, _, _, 20],
    [1, _, 3, _, _, 6, 7, _, 9, 10, 11, _, 13, _, 15, _, 17, 18, _, 20],
    [1, _, 3, 4, _, 6, _, _, 9, _, _, _, 13, _, 15, _, 17, 18, _, 20],
    [1, _, 3, 4, _, 6, 7, _, _, 10, _, 12, 13, _, 15, _, 17, _, _, 20],
    [1, 'c', _, _, _, 6, 7, _, 9, _, _, _, 13, _, 15, _, 17, 18, _, 20],
    [1, _, 3, 4, _, 6, 7, _, 9, 10, _, 12, 13, _, 15, _, _, 18, _, 20],
    [1, _, 3, 4, _, _, 7, _, _, 10, _, _, 13, _, 15, _, 17, 18, _, 20],
    [1, _, 3, 4, _, 6, _, _, 9, _, 11, _, 13, _, 15, 16, _, _, _, 20],
    [1, _, _, _, _, 6, 7, _, 9, _, 11, _, 13, _, 15, 16, 17, _, 19, 20],
    [1, _, 3, 4, _, _, _, _, 9, _, 11, _, 13, 'c', 15, _, _, _, 19, 20],
    [1, 'p', 3, 4, 'c', 6, 7, _, 9, _, 11, _, 13, _, 15, _, 17, _, 19, 20],
    [1, 'c', _, 4, _, 6, _, _, _, _, 11, _, 13, _, _, _, 17, _, 19, 20],
    [1, _, 3, 4, _, 6, _, 8, 9, _, 11, _, 13, _, 15, _, 17, _, 19, 20],
    [1, _, _, 4, _, _, 'c', _, _, _, 11, _, 13, _, 15, _, 17, _, 19, 20],
    [1, _, 3, 4, 5, 6, 7, 8, 9, _, _, _, _, _, _, _, _, 18, _, 20],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
]

WIDTH = len(MAP) * BLOCKSIZE
HEIGHT = len(MAP[0]) * BLOCKSIZE