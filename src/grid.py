import pygame

class Grid:
    def __init__(self, w : int, h : int):
        self.w :int= w
        self.h :int= h
        self.grid = self.create_grid()
        self.next_grid = self.create_grid()

    def create_grid(self, active_default = False) -> list[bool]:
        grd = []

        for y in range(self.h):
            for x in range(self.w):
                grd.append(active_default)

        return grd

    def set_cell(self, x : int, y : int, active : bool):
        ux = x % self.w
        uy = y % self.h
        index = uy * self.w + ux

        self.next_grid[index] = active

    def get_cell(self, x : int, y : int) -> bool:
        ux = x % self.w
        uy = y % self.h
        index = uy * self.w + ux

        return self.grid[index]

    def clear(self):
        self.grid = self.create_grid()
        self.next_grid = self.create_grid()

    def update(self):
        self.grid = self.next_grid
        self.next_grid = self.create_grid()

    def draw(self, window, death_color, birth_color, cell_w, cell_h):
        for i, death in enumerate(self.grid):
            if death:
                x = i % self.w
                y = i // self.w

                pygame.draw.rect(window, death_color, [x * cell_w, y * cell_h, cell_w + 1, cell_h + 1])

        for i, birth in enumerate(self.next_grid):
            if birth:
                x = i % self.w
                y = i // self.w

                pygame.draw.rect( window, birth_color, [x * cell_w, y * cell_h, cell_w + 1, cell_h + 1])