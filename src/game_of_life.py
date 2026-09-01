import pygame, random
from app import *
from grid import *


class GameOfLife(App):
    def __init__(self,  grid_w, grid_h):
        super().__init__(app_params=AppParams(1280, 720, "Toroidal Game Of Life", 60, [0, 0, 0]))
        self.cell_w = self.app_params.w / grid_w
        self.cell_h = self.app_params.h / grid_h

        self.grid = Grid(grid_w, grid_h)
        self.cell_active_color = [255, 255, 255]

    def update(self):
        self.grid.clear()

        for i in range(30):
            rng_x = random.randrange(0, self.grid.w)
            rng_y = random.randrange(0, self.grid.h)

            self.grid.set_cell(rng_x, rng_y, True)

    def draw(self):
        self.window.fill(self.app_params.bgc)
        self.draw_grid()
        pygame.display.update()

    def draw_grid(self):
        for y in range(self.grid.h):
            for x in range(self.grid.w):
                cell = self.grid.get_cell(x, y)
                if cell == True:
                    pygame.draw.rect(self.window, self.cell_active_color, [x * self.cell_w, y * self.cell_h, self.cell_w, self.cell_h])