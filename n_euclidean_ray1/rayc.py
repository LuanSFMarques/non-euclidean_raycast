import pygame as pg
import math

from settings import *
from mini_map import mini_map


class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox1, oy1 = self.game.player.pos_1 # Not divided by pieces
        ox2, oy2 = self.game.player.pos_2 # Divided by pieces
        x_map1, y_map1 = self.game.player.map_pos_1 # Not divided by pieces
        x_map2, y_map2 = self.game.player.map_pos_2 # Divided by pieces

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS): #num of rays

            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Horizontal Analysis --------------------------------------------------
            y_hor, dy = ((y_map2 + 1)*PIECES_SIZE, 1) if sin_a > 0 else ((y_map2 - 1e-6)*PIECES_SIZE, -1)

            if sin_a == 0:  #Division by zero correction
                sin_a = 1e-6
            depth_hor = (y_hor - oy1) / sin_a
            x_hor = ox1 + depth_hor * cos_a

            delta_depth_hor = dy*PIECES_SIZE / sin_a
            dx = delta_depth_hor * cos_a

            its_wall_hor = True

            # Clone Vision for illusion
            clone1 = False
            clone2 = False

            dxhor = dx
            dyhor = dy
            # Ray Distance
            for i in range(MAX_DEPTH):
                tile_vert = int(x_hor)//PIECES_SIZE, int(y_hor)//PIECES_SIZE
                if tile_vert in self.game.map.world_map:
                    break
                elif tile_vert in self.game.map.world_portals:
                    its_wall_hor = False
                    if self.game.map.world_portals[tile_vert] == 1:
                        clone1 = True
                    else:
                        clone2 = True
                    break
                x_hor += dx
                y_hor += dy*PIECES_SIZE
                depth_hor += delta_depth_hor
            final_hor = tile_vert

            # Vertical Analysis --------------------------------------------------
            x_vert, dx = ((x_map2 + 1)*PIECES_SIZE, 1) if cos_a > 0 else ((x_map2 - 1e-6)*PIECES_SIZE, -1)

            depth_vert = (x_vert - ox1) / cos_a

            clone_depth_vert = depth_vert

            y_vert = oy1 + depth_vert * sin_a

            aaax = x_vert
            aaay = y_vert

            delta_depth_vert = dx*PIECES_SIZE / cos_a

            dy = delta_depth_vert * sin_a
            its_wall_vert = True

            dxvert = dx
            dyvert = dy
            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert)//PIECES_SIZE, int(y_vert)//PIECES_SIZE
                if tile_vert in self.game.map.world_map:
                    break
                elif tile_vert in self.game.map.world_portals:
                    its_wall_vert = False
                    break
                x_vert += dx*PIECES_SIZE
                y_vert += dy
                depth_vert += delta_depth_vert
            final_vert = tile_vert

            # Depth
            if depth_vert < depth_hor:
                depth = depth_vert
                final_final = final_vert
                its_wall = its_wall_vert
            else:
                depth = depth_hor
                final_final = final_hor
                its_wall = its_wall_hor

            # Collision with portals and vision switch
            if its_wall == its_wall_hor and its_wall == False:

                depth_hor_clone = depth_hor
                depth_vert_clone = depth_vert

                if self.game.map.world_portals[final_final] == 1:
                    
                    # HORIZONTAL

                    x_clone_hor = x_hor - (7 * PIECES_SIZE)
                    y_clone_hor = y_hor - (2 * PIECES_SIZE)


                    for _ in range(20):
                        tile_clone_hor = int(x_clone_hor)//PIECES_SIZE, int(y_clone_hor)//PIECES_SIZE
                        if tile_clone_hor in self.game.map.clone1:
                            if self.game.map.clone1[tile_clone_hor] == 1:
                                color_clone_hor = True
                            else:
                                color_clone_hor = False
                            break
                        x_clone_hor += dxhor
                        y_clone_hor += dyhor * PIECES_SIZE
                        depth_hor_clone += delta_depth_hor

                        
                    # VERTICAL

                    x_clone_vert = aaax - (7 * PIECES_SIZE)
                    y_clone_vert = aaay - (2 * PIECES_SIZE)


                    for _ in range(20):
                        tile_clone_vert = int(x_clone_vert)//PIECES_SIZE, int(y_clone_vert)//PIECES_SIZE
                        if tile_clone_vert in self.game.map.clone1:
                            if self.game.map.clone1[tile_clone_vert] == 1:
                                color_clone_vert = True
                            else:
                                color_clone_vert = False
                            break
                        x_clone_vert += dxvert * PIECES_SIZE 
                        y_clone_vert += dyvert
                        clone_depth_vert += delta_depth_vert

                    # FINAL CLONE CALC

                    if clone_depth_vert < depth_hor_clone:
                        depth = clone_depth_vert
                        x_clone = x_clone_vert
                        y_clone = y_clone_vert

                        color_clone = color_clone_vert

                        final_final = (x_clone,y_clone)
                    else:
                        depth = depth_hor_clone
                        x_clone = x_clone_hor
                        y_clone = y_clone_hor

                        color_clone = color_clone_hor

                        final_final = (x_clone,y_clone)


                else:
                    #HORIZONTAL
                    x_clone_hor = x_hor - (7 * PIECES_SIZE)
                    y_clone_hor = y_hor + (2 * PIECES_SIZE)

                    for _ in range(20):
                        tile_clone_hor = int(x_clone_hor)//PIECES_SIZE, int(y_clone_hor)//PIECES_SIZE
                        if tile_clone_hor in self.game.map.clone2:
                            if self.game.map.clone2[tile_clone_hor] == 1:
                                color_clone_hor = True
                            else:
                                color_clone_hor = False
                            break
                        x_clone_hor += dxhor
                        y_clone_hor += dyhor * PIECES_SIZE
                        depth_hor_clone += delta_depth_hor

                    #VERTICAL
                    x_clone_vert = aaax - (7 * PIECES_SIZE)
                    y_clone_vert = aaay + (2 * PIECES_SIZE)



                    for _ in range(20):
                        tile_clone_vert = int(x_clone_vert)//PIECES_SIZE, int(y_clone_vert)//PIECES_SIZE
                        if tile_clone_vert in self.game.map.clone2:
                            if self.game.map.clone2[tile_clone_vert] == 1:
                                color_clone_vert = True
                            else:
                                color_clone_vert = False
                            break
                        x_clone_vert += dxvert * PIECES_SIZE 
                        y_clone_vert += dyvert
                        clone_depth_vert += delta_depth_vert

                    if clone_depth_vert < depth_hor_clone:
                        depth = clone_depth_vert
                        x_clone = x_clone_vert
                        y_clone = y_clone_vert

                        color_clone = color_clone_vert

                        final_final = (x_clone,y_clone)
                    else:
                        depth = depth_hor_clone
                        x_clone = x_clone_hor
                        y_clone = y_clone_hor

                        color_clone = color_clone_hor

                        final_final = (x_clone,y_clone)


            # FishBowl Remove
            depth3d = depth * math.cos(self.game.player.angle - ray_angle)

            # Projection
            wall_height = 50000 / (depth3d + 0.0001)
            if wall_height > HEIGHT: wall_height == HEIGHT


            # Draw Walls
            try:
                if self.game.map.world_map[final_final] == 1:
                    wall_color = [161 / (1 + depth3d ** 5 * 0.000000000000002), 151 / (1 + depth3d ** 5 * 0.000000000000002),191 / (1 + depth3d ** 5 * 0.000000000000002)]
                else:
                    wall_color = [215 / (1 + depth3d ** 5 * 0.000000000000002), 202 / (1 + depth3d ** 5 * 0.000000000000002),255 / (1 + depth3d ** 5 * 0.000000000000002)]
                line_color = 'yellow'
            except:
                try:
                    if color_clone:
                        wall_color = [161 / (1 + depth3d ** 5 * 0.000000000000002), 151 / (1 + depth3d ** 5 * 0.000000000000002),191 / (1 + depth3d ** 5 * 0.000000000000002)]
                    else:
                        wall_color = [215 / (1 + depth3d ** 5 * 0.000000000000002), 202 / (1 + depth3d ** 5 * 0.000000000000002),255 / (1 + depth3d ** 5 * 0.000000000000002)]
                except:
                    wall_color = 'black'
                line_color = 'yellow'

            pg.draw.rect(self.game.screen, wall_color, (ray * SCALE,(HEIGHT/2) - wall_height // 2, SCALE, wall_height))

            # Draw Lines 2d

            # Draw Lines 2d CLONE
            if clone1:
                cx1, cy1 = ox1 - (PIECES_SIZE*7), oy1 - (PIECES_SIZE*2)

            elif clone2:
                cx1, cy1 = ox1 - (PIECES_SIZE*7), oy1 + (PIECES_SIZE*2)


            # Draw Lines 3d CLONE



            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()

