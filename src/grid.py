import pygame


class Grid:
    def __init__(self, w: int, h: int, cell_w: int, cell_h: int, birth_color):
        self.w: int = w
        self.h: int = h
        self.cell_w: int = cell_w
        self.cell_h: int = cell_h

        self.prev_grid = self.create_grid()
        self.grid = self.create_grid()
        self.next_grid = self.create_grid()

        self.grid_tx =         pygame.Surface([w * cell_w, h * cell_h]).convert_alpha()
        self.grid_tx.fill((0, 0, 0))

        self.birth_color = birth_color

    def create_grid(self, active_default=False) -> list[bool]:
        grd = []

        for y in range(self.h):
            for x in range(self.w):
                grd.append(active_default)

        return grd

    def set_cell(self, x: int, y: int, active: bool):
        ux = x % self.w
        uy = y % self.h
        index = uy * self.w + ux
        color = [0, 0, 0]

        self.next_grid[index] = active

        if active:
            color = self.birth_color

        pygame.draw.rect(self.grid_tx, color,[ux * self.cell_w, uy * self.cell_h, self.cell_w + 1, self.cell_h + 1])

    def get_cell(self, x: int, y: int) -> bool:
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
        self.grid_tx.fill((0, 0, 0, 0))

    def draw(self, window : pygame.Surface):
        window.blit(self.grid_tx, (0, 0))