import pygame as pg
import sys

from settings import *
from mini_map import *
from player import *
from rayc import *

class Game:
    # Initializer
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    # ??
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.rayc = RayCasting(self)

    # Update informations
    def update(self):
        self.player.update()
        self.rayc.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'Non-Euclidean Environment in a Ray Casting World       \n{self.clock.get_fps() :.0f}')  #Title

    # Draw the visuals
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    # Check Commands (for quit)
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    # Run class functions (in loop)
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

# Running the program
if __name__ == '__main__':
    rayCastingSim = Game()
    rayCastingSim.run()