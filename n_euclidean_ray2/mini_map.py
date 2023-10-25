import pygame as pg

from settings import *

mini_map = [ 
    [2,1,2,1,2,1,2,1,2,1],
    [1,0,0,0,0,0,0,0,0,2],
    [2,0,1,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,2],
    [2,0,1,0,0,0,0,2,0,1],
    [1,0,2,0,0,0,0,1,0,2],
    [2,0,1,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,1],
    [1,2,1,2,1,2,1,2,1,2]
]

portals = [ #(8,4) (8,5)
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,2,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

clone_map_1 = [ #(1,2)
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [2,0,1,0,0,0,0,0,0,0],
    [1,0,2,0,0,0,0,0,0,0],
    [2,0,1,0,0,0,0,0,0,0],
    [1,0,2,0,0,0,0,0,0,0],
    [2,0,1,0,0,0,0,0,0,0],
    [1,0,2,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0],
    [1,2,1,2,0,0,0,0,0,0]
]

clone_map_2 = [ # (1,7)
    [2,1,2,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [2,0,1,0,0,0,0,0,0,0],
    [1,0,2,0,0,0,0,0,0,0],
    [2,0,1,0,0,0,0,0,0,0],
    [1,0,2,0,0,0,0,0,0,0],
    [2,0,1,0,0,0,0,0,0,0],
    [1,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.portals = portals
        self.c1 = clone_map_1
        self.c2 = clone_map_2
        self.world_map = {}
        self.world_portals = {}
        self.clone1 = {}
        self.clone2 = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
        
        for j, row in enumerate(self.portals):
            for i, value in enumerate(row):
                if value:
                    self.world_portals[(i, j)] = value

        for j, row in enumerate(self.c1):
            for i, value in enumerate(row):
                if value:
                    self.clone1[(i, j)] = value

        for j, row in enumerate(self.c2):
            for i, value in enumerate(row):
                if value:
                    self.clone2[(i, j)] = value

    def draw(self):
        pg.draw.rect(self.game.screen,(0,0,0),(0,0,HEIGHT,HEIGHT))
        pg.draw.rect(self.game.screen, (137,128,162), (WIDTH//3, HEIGHT/2, HEIGHT, HEIGHT))
        pg.draw.rect(self.game.screen, (10, 10, 10), (WIDTH//3, -HEIGHT/2, HEIGHT, HEIGHT))

        for pos in self.world_map:
            
            pg.draw.rect(
                self.game.screen,
                C_TILE1 if self.world_map[(pos[0]), (pos[1])] == 1 else C_TILE2,
                (pos[0] * PIECES_SIZE, pos[1] * PIECES_SIZE, PIECES_SIZE, PIECES_SIZE)
                )
            '''
            pg.draw.rect(
                self.game.screen,
                C_TILE1 if self.world_map[(pos[0]), (pos[1])] == 1 else C_TILE_DETEC,
                ((2*WIDTH//3)+(pos[0] * PIECES_SIZE), pos[1] * PIECES_SIZE, PIECES_SIZE - 2, PIECES_SIZE - 2)
                )
            ''' 
        for pos in self.world_map:
            pg.draw.rect(
                self.game.screen,
                C_TILE_BORDER,
                ((2*WIDTH//3)+(pos[0] * PIECES_SIZE), pos[1] * PIECES_SIZE, PIECES_SIZE, PIECES_SIZE)
                )
