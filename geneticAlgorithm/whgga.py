import os
import sys
os.chdir(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
import argparse
from uuid import uuid4
import json
from random import randint
from whg import WHG
from bullets import Bullet
from board import BoardL30
from geneticAlgorithm.genAlgorithm import GeneticAlgorithm
from geneticAlgorithm.agentga import AgentGA
import pygame

class WHGGA(WHG):
    NUMOFAGENTS = 100
    MOVES = 250
    
    def __init__(self):
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.board = BoardL30()
        self.bullets = Bullet.create_bullets(Bullet)
        self.agents = pygame.sprite.Group()
        self.geneticAlg = GeneticAlgorithm()
        for i in range(self.NUMOFAGENTS):
            self.agents.add(AgentGA())
        self.generation = 0
        
    def run(self, path=None):
        pygame.init()
        running = True
        self.geneticAlg.initializeGenerationZero(agents=self.agents.sprites(), moves=self.MOVES, path=path)
        while running:
            self.run_generation()
            self.generation += 1
            newAgents = self.geneticAlg.initializeNextGeneration(self.agents.sprites(), self.NUMOFAGENTS)
            self.restart_game(newAgents)
            running = not self.did_user_quit()
        pygame.quit()
            
    def run_generation(self):
        move = 0
        while move < self.MOVES:
            for agent in self.agents.sprites():
                agent.move(self.board, self.dt, move)
            self.draw()
            self.handle_collisions()
            self.bullets.update()
            pygame.display.flip()
            self.dt = self.clock.tick(self.FPS) / 1000
            move += 1
        
    def draw(self):
        self.display.fill(self.BAR_COLOUR)
        self.draw_background()
        self.draw_attributes()
        self.board.draw(self.display)
        for agent in self.agents.sprites():
            agent.draw(self.display)
            agent.coins.draw(self.display)
        self.bullets.draw(self.display)
    

    def draw_attributes(self):
        font = pygame.font.SysFont(self.FONT_NAME, self.FONT_SIZE)
        levelText = f'LEVEL: {self.LEVEL}'
        aliveText = f'ALIVE: {self.numOfAgentsAlive()}'
        genText = f'GEN: {self.generation}'
        self.draw_text(levelText, font, self.FONT_COLOUR, (10, 15))
        self.draw_text(aliveText, font, self.FONT_COLOUR, (350, 15))
        self.draw_text(genText, font, self.FONT_COLOUR, (750, 15))

            
    def handle_collisions(self):
        for agent in self.agents.sprites():
            if pygame.sprite.spritecollide(agent, self.bullets, False):
                if pygame.sprite.spritecollide(agent, self.bullets, False, pygame.sprite.collide_mask):
                    agent.isAlive = False
            elif pygame.sprite.spritecollide(agent, agent.coins, False):
                if pygame.sprite.spritecollide(agent, agent.coins, True, pygame.sprite.collide_mask):
                    agent.coinsCaught += 1
                    
    def restart_game(self, newAgents):
        for agent in self.agents.sprites():
            agent.coins.empty()
        self.agents.empty()
        self.agents = newAgents
        self.bullets.empty()
        self.bullets = Bullet.create_bullets(Bullet)
                    
    def numOfAgentsAlive(self):
        agentsAlive = 0
        for agent in self.agents.sprites():
            if agent.isAlive:
                agentsAlive += 1
        return agentsAlive
    
    def saveData(self, dstDir):
        fileName = f'{uuid4()}.json'
        dstPath  = os.path.join(dstDir, fileName)
        data = {}
        data["movesNum"] = self.MOVES
        data["agentsNum"] = self.NUMOFAGENTS
        data["moves"] = []
        with open(dstPath, "w") as resultFile:
            for agent in self.agents.sprites():
                data["moves"].append(agent.moves)
            json.dump(data, resultFile, indent=4)
                    
if __name__ == '__main__':
    print('running WHGGA run')
    whg = WHGGA()
    whg.run()