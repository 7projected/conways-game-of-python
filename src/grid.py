class Grid:
    def __init__(self, w : int, h : int):
        self.w :int= w
        self.h :int= h
        self.grid = []

        self.create_grid()

    def create_grid(self):
        self.grid.clear()

        for y in range(self.h):
            for x in range(self.w):
                self.grid.append(False)

    def set_cell(self, x : int, y : int, active : bool):
        ux = x % self.w
        uy = y % self.h
        index = uy * self.w + ux

        self.grid[index] = active

    def get_cell(self, x : int, y : int) -> bool:
        ux = x % self.w
        uy = y % self.h
        index = uy * self.w + ux

        return self.grid[index]

    def clear(self):
        self.create_grid()