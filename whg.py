import pygame
from board import BoardL30
from agent import Agent
from bullets import Bullets
from coins import Coins


class WHG:

    WIDTH = 900
    HEIGHT = 705
    FPS = 60
    __BAR_COLOUR = "black"
    __BAR_HEIGHT = 60
    __BACKGROUND_POSITION = pygame.Vector2(0, __BAR_HEIGHT)
    __BACKGROUND_DIMENSIONS = pygame.Vector2(
        WIDTH, HEIGHT - (2 * __BAR_HEIGHT))

    def __init__(self, width=WIDTH, height=HEIGHT, fps=FPS):
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = fps
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.board = BoardL30()
        self.agent = Agent(self.WIDTH / 2, self.HEIGHT / 2)
        self.bullets = Bullets()
        self.coins = Coins()
        self.coinsCaught = 0
        self.fails = 0

    def run(self):
        pygame.init()
        running = True
        while running:
            running = not self.did_user_quit()
            self.agent.user_move(self.board.get_body(), self.dt)
            self.draw()
            pygame.display.flip()
            self.dt = self.clock.tick(self.FPS) / 1000
        pygame.quit()

    def draw(self):
        self.display.fill(self.__BAR_COLOUR)
        self.draw_background()
        self.board.draw(self.display)
        self.agent.draw(self.display)

    def draw_background(self):
        pygame.draw.rect(self.display, self.board.BACKGROUND_COLOUR,
                         pygame.Rect(self.__BACKGROUND_POSITION, self.__BACKGROUND_DIMENSIONS))

    def did_user_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False


if __name__ == '__main__':
    whg = WHG()
    whg.run()
