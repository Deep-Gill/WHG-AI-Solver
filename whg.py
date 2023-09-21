import pygame
import time
from board import BoardL30
from agent import Agent
from bullets import Bullet
from coins import Coin


class WHG:

    LEVEL = 30
    WIDTH = 900
    HEIGHT = 705
    FPS = 60
    __BAR_COLOUR = "black"
    __BAR_HEIGHT = 60
    __BACKGROUND_POSITION = pygame.Vector2(0, __BAR_HEIGHT)
    __BACKGROUND_DIMENSIONS = pygame.Vector2(WIDTH, HEIGHT - (2 * __BAR_HEIGHT))
    __FONT_NAME = "Corbel"
    __FONT_SIZE = 45
    __FONT_COLOUR = "white"

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
            if self.is_game_completed(): break
            self.agent.user_move(self.board, self.dt)
            self.draw()
            self.handle_collisions()
            pygame.display.flip()
            self.dt = self.clock.tick(self.FPS) / 1000
        pygame.quit()
        
    def restart_game(self):
        self.coins.remove()
        self.bullets.remove()
        self.bullets = Bullet.create_bullets(Bullet)
        self.coins = Coin.create_coins(Coin)
        self.agent.rect.x = self.agent.INITIAL_POSITION.x
        self.agent.rect.y = self.agent.INITIAL_POSITION.y
        self.agent.coinsCaught = 0
        
        
    def is_game_completed(self):
        if self.agent.coinsCaught == Coin.TOTAL and self.board.is_inside_goal(self.agent.rect):
                self.draw_game_completed_screen()
                time.sleep(2)
                return True
        return False
        
    def handle_collisions(self):
        if pygame.sprite.spritecollide(self.agent, self.bullets, False):
            if pygame.sprite.spritecollide(self.agent, self.bullets, False, pygame.sprite.collide_mask):
                self.agent.fails += 1
                self.restart_game()
        elif pygame.sprite.spritecollide(self.agent, self.coins, False):
            if pygame.sprite.spritecollide(self.agent, self.coins, True, pygame.sprite.collide_mask):
                self.agent.coinsCaught += 1


    def draw(self):
        self.display.fill(self.__BAR_COLOUR)
        self.draw_background()
        self.draw_attributes()
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
        

    def draw_game_completed_screen(self):
        self.display.fill((0, 0, 0))
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Congratulations! You completed level 30!", True, (255, 255, 255))  
        text_rect = game_over_text.get_rect(center=(self.display.get_width() // 2, self.display.get_height() // 2))
        self.display.blit(game_over_text, text_rect)  
        pygame.display.flip()  

    def draw_text(self, text, font, colour, position):
        textImg = font.render(text, True, colour)
        self.display.blit(textImg, position)
    
    def draw_attributes(self):
        font = pygame.font.SysFont(self.__FONT_NAME, self.__FONT_SIZE)
        failsText = f'FAILS: {self.agent.fails}'
        coinsText = f'COINS: {self.agent.coinsCaught}/{Coin.TOTAL}'
        levelText = f'LEVEL: {self.LEVEL}'
        self.draw_text(levelText, font, self.__FONT_COLOUR, (10, 15))
        self.draw_text(coinsText, font, self.__FONT_COLOUR, (350, 15))
        self.draw_text(failsText, font, self.__FONT_COLOUR, (750, 15))
        
    def draw_buttons(self):
        pass
        

if __name__ == '__main__':
    whg = WHG()
    whg.run()


