import pygame as pg
import math


from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS_1
        self.angle = PLAYER_ANGLE_1

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED_1 * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos


        
        self.check_wall_collision(dx, dy)
        self.check_portal_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_RSPEED_1 * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_RSPEED_1 * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x//PIECES_SIZE, y//PIECES_SIZE) not in self.game.map.world_map 

    def check_portal(self, x, y):
        return (x//PIECES_SIZE, y//PIECES_SIZE) not in self.game.map.world_portals

    def check_portal_collision(self, dx, dy):
        if not self.check_portal(int(self.x), int(self.y)):
            delta_size = self.x % PIECES_SIZE
            # Portal 1
            if self.game.map.world_portals[self.x//PIECES_SIZE, self.y//PIECES_SIZE] == 1:
                self.x = PIECES_SIZE + delta_size
                self.y = 2*PIECES_SIZE + 1 # Pos Correction
            # Portal 2
            else:
                self.x = PIECES_SIZE + delta_size
                self.y = 8*PIECES_SIZE - 1 # Pos Correction

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pg.draw.circle(self.game.screen, 'green', (self.x+HEIGHT_2, self.y), 8)



    def update(self):
        self.movement()

    @property
    def pos_2(self):
        return self.x/PIECES_SIZE, self.y/PIECES_SIZE
    
    @property
    def pos_1(self):
        return self.x, self.y
    
    @property
    def map_pos_1(self):
        return int(self.x), int(self.y)
    
    @property
    def map_pos_2(self):
        return int(self.x)//PIECES_SIZE, int(self.y)//PIECES_SIZE