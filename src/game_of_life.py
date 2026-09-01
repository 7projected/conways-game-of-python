import pygame, random
from app import *
from grid import *


class GameOfLife(App):
    def __init__(self,  grid_w, grid_h):
        super().__init__(app_params=AppParams(1280, 720, "Toroidal Game Of Life", 5, [0, 0, 0]))
        self.cell_w = self.app_params.w / grid_w
        self.cell_h = self.app_params.h / grid_h

        self.grid = Grid(grid_w, grid_h)
        self.cell_active_color = [255, 255, 255]

        self.grid.set_cell(1, 1, True)
        self.frame = 0

    def update(self):
        self.frame += 1

        for y in range(self.grid.h):
            for x in range(self.grid.w):
                get_value = self.grid.get_cell(x, y)

                if get_value == True:
                    self.grid.set_cell(x + 1, y + 1, True)
                    self.grid.set_cell(x, y + 1, True)
                    self.grid.set_cell(x + 1, y, True)

        self.grid.draw(self.window, [255, 0, 0], [255, 255, 255], self.cell_w, self.cell_h)
        self.grid.update()
