import pygame
import time
from board import BoardL30
from agent import Agent
from bullets import Bullet
from coins import Coin


class WHG:

    WIDTH = 900
    HEIGHT = 705
    FPS = 60
    __BAR_COLOUR = "black"
    __BAR_HEIGHT = 60
    __BACKGROUND_POSITION = pygame.Vector2(0, __BAR_HEIGHT)
    __BACKGROUND_DIMENSIONS = pygame.Vector2(
        WIDTH, HEIGHT - (2 * __BAR_HEIGHT))


    def __init__(self):
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.board = BoardL30()
        self.agent = Agent()
        self.bullets = Bullet.create_bullets(Bullet)
        self.coins = Coin.create_coins(Coin)
        


    def run(self):
        pygame.init()
        running = True
        while running:
            running = not self.did_user_quit()
            if pygame.sprite.spritecollide(self.agent, self.coins, True, pygame.sprite.collide_mask):
                # self.agent.coinsCaught += self.agent.coinsCaught
                pass
            if pygame.sprite.spritecollide(self.agent, self.bullets, False, pygame.sprite.collide_mask):
                # self.agent.fails += self.agent.fails
                self.game_over_screen()
                time.sleep(2)
                break 
            self.agent.user_move(self.board, self.dt)
            self.draw()
            pygame.display.flip()
            self.dt = self.clock.tick(self.FPS) / 1000
        pygame.quit()


    def draw(self):
        self.display.fill(self.__BAR_COLOUR)
        self.draw_background()
        self.board.draw(self.display)
        self.agent.draw(self.display)
        self.coins.draw(self.display)
        self.bullets.draw(self.display)
        self.bullets.update()


    def draw_background(self):
        pygame.draw.rect(self.display, self.board.BACKGROUND_COLOUR,
                         pygame.Rect(self.__BACKGROUND_POSITION, self.__BACKGROUND_DIMENSIONS))

    def did_user_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    

    def game_over_screen(self):
        self.display.fill((0, 0, 0))
        font = pygame.font.Font(None, 48) 
        game_over_text = font.render("Game Over Sucker", True, (255, 255, 255))  
        text_rect = game_over_text.get_rect(center=(self.display.get_width() // 2, self.display.get_height() // 2))
        self.display.blit(game_over_text, text_rect)  
        pygame.display.flip()  


if __name__ == '__main__':
    whg = WHG()
    whg.run()


