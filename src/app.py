import pygame

class AppParams:
    def __init__(self, w, h, title, fps, bgc):
        self.w = w
        self.h = h
        self.title = title
        self.fps = fps
        self.bgc = [0, 0, 0]


class App:
    def __init__(self, app_params : AppParams):
        self.app_params = app_params
        
        pygame.init()

        self.window = pygame.display.set_mode([self.app_params.w, self.app_params.h])
        pygame.display.set_caption(self.app_params.title)

        self.clock = pygame.time.Clock()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            dt = self.clock.tick(self.app_params.fps)
            self.update()
            self.draw()

    def draw(self):
        pass

    def update(self):
        pass