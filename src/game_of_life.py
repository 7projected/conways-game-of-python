import pygame, random
from app import *
from grid import *


class GameOfLife(App):
    def __init__(self,  grid_w, grid_h, frames_per_update, toroidal : bool):
        name_str = "Toroidal Game Of Life"
        if not toroidal:
            name_str = "Game Of Life"


        super().__init__(app_params=AppParams(1280, 720, name_str, 60, [0, 0, 0]))
        self.cell_w = self.app_params.w / grid_w
        self.cell_h = self.app_params.h / grid_h

        self.grid = Grid(grid_w, grid_h, self.cell_w, self.cell_h, toroidal, [255, 255, 255])
        self.cell_active_color = [255, 255, 255]

        self.grid.set_cell(1, 1, True)
        self.grid.set_cell(2, 1, True)
        self.grid.set_cell(3, 1, True)

        self.frames_per_update = frames_per_update
        self.frame = 0
        self.paused = False

        self.pause_icon_lifetime = 0
        self.max_pause_icon_lifetime = self.app_params.fps
        self.toggle_pause()

    def toggle_pause(self):
        self.paused = not self.paused
        self.pause_icon_lifetime = self.max_pause_icon_lifetime 

        if self.paused:
            self.pause_icon_surf = pygame.image.load("./png/pause.png")
        else:
            self.pause_icon_surf = pygame.image.load("./png/unpause.png")


    def draw_pause_icon(self):
        if self.pause_icon_lifetime > 0:
            center = [self.app_params.w / 2, self.app_params.h / 2]
            pos = [center[0] - self.pause_icon_surf.get_width() / 2, center[1] - self.pause_icon_surf.get_height() / 2]
            self.window.blit(self.pause_icon_surf, pos)

    def paint_cell_at_mouse(self):
        mouse = pygame.mouse.get_pos()

        c = [int(mouse[0] / self.cell_w), int(mouse[1] / self.cell_h)]

        self.grid.set_cell(c[0], c[1], True)
        self.grid.update(False)

    def erase_cell_at_mouse(self):
        mouse = pygame.mouse.get_pos()

        c = [int(mouse[0] / self.cell_w), int(mouse[1] / self.cell_h)] 

        self.grid.set_cell(c[0], c[1], False)
        self.grid.update(False)
    
    def draw_mouse_grid_pos(self):
        mouse = pygame.mouse.get_pos()

        c = [int(mouse[0] / self.cell_w), int(mouse[1] / self.cell_h)] 

        pygame.draw.rect(self.window, [255, 0, 0], [c[0] * self.cell_w, c[1] * self.cell_h, self.cell_w, self.cell_h], 2)


    def manage_mouse(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.paint_cell_at_mouse()
        if mouse[2]:
            self.erase_cell_at_mouse()


    def step(self):
        self.grid.update()
        
        for y in range(self.grid.h):
            for x in range(self.grid.w):
                # For each cell
                get_value = self.grid.get_cell(x, y)
                alive_next_iter = False

                neighbors = 0
                for nx in range(3):
                    for ny in range(3):
                        used_x = nx - 1
                        used_y = ny - 1
                        
                        if used_x == 0 and used_y == 0:
                            pass
                        else:
                            if self.grid.get_cell(x + used_x, y + used_y) == True:
                                neighbors += 1


                if get_value == True:
                    if neighbors > 3:
                        alive_next_iter = False
                    if neighbors < 2:
                        alive_next_iter = False
                    if neighbors == 2:
                        alive_next_iter = True
                    if neighbors == 3:
                        alive_next_iter = True
                else:
                    if neighbors == 3:
                        alive_next_iter = True

                self.grid.set_cell(x,y,alive_next_iter)

        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.toggle_pause()
                if event.key == pygame.K_EQUALS:
                    self.frames_per_update -= 5
                    if self.frames_per_update <= 0: self.frames_per_update = 5
                    print(self.frames_per_update)
                if event.key == pygame.K_MINUS:
                    self.frames_per_update += 5
                    print(self.frames_per_update)

        self.manage_mouse()

        if not self.paused:
            self.frame += 1
        self.pause_icon_lifetime -= 1

        self.grid.draw(self.window)
        self.draw_pause_icon()
        self.draw_mouse_grid_pos()

        if (self.frame >= self.frames_per_update):
            self.frame = 0
            self.step()