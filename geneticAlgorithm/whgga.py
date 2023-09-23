import os
import sys
os.chdir(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from whg import WHG
from bullets import Bullet
from board import BoardL30
from geneticAlgorithm.agentga import AgentGA
import pygame

class WHGGA(WHG):
    NUMOFAGENTS = 100
    MOVES = 1000
    
    def __init__(self):
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.board = BoardL30()
        self.bullets = Bullet.create_bullets(Bullet)
        self.agents = pygame.sprite.Group()
        for i in range(self.NUMOFAGENTS):
            self.agents.add(AgentGA())
        print(self.agents)
            
    def run(self):
        pygame.init()
        running = True
        move = 0
        while running and move < self.MOVES:
            running = not self.did_user_quit()
            for agent in self.agents.sprites():
                agent.move(self.board, self.dt)
            self.draw()
            self.handle_collisions()
            self.bullets.update()
            pygame.display.flip()
            self.dt = self.clock.tick(self.FPS) / 1000
            move += 1
        pygame.quit()
        
    def draw(self):
        self.display.fill(self.BAR_COLOUR)
        self.draw_background()
        self.board.draw(self.display)
        self.agents.draw(self.display)
        for agent in self.agents.sprites():
            agent.coins.draw(self.display)
        self.bullets.draw(self.display)
            
    def handle_collisions(self):
        for agent in self.agents.sprites():
            if pygame.sprite.spritecollide(agent, self.bullets, False):
                if pygame.sprite.spritecollide(agent, self.bullets, False, pygame.sprite.collide_mask):
                    agent.isAlive = False
                    agent.move_pos(agent.INITIAL_POSITION.x, agent.INITIAL_POSITION.y)
            elif pygame.sprite.spritecollide(agent, agent.coins, False):
                if pygame.sprite.spritecollide(agent, agent.coins, True, pygame.sprite.collide_mask):
                    agent.coinsCaught += 1
                    
                    
if __name__ == '__main__':
    print('running WHGGA run')
    whg = WHGGA()
    whg.run()