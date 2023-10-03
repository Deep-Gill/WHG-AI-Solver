import os
os.chdir(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from agent import Agent
from coins import Coin
from random import randint
from enum import IntEnum

class Moves(IntEnum):
    MOVE_TOP = 0
    MOVE_LEFT = 1
    MOVE_BOTTOM = 2
    MOVE_RIGHT = 3
    NO_MOVE = 4

class AgentGA(Agent):
    def __init__(self):
        super().__init__()
        self.coins = Coin.create_coins(Coin)
        self.isAlive = True
        self.moves = []
        self.movesTaken = 0
        self.fitnessScore = 0
        
    def draw(self, screen):
        if self.isAlive: 
            super().draw(screen)
        
    def move(self, board, dt, moveNum):
        if self.isAlive:
            match self.moves[moveNum]:
                case Moves.MOVE_TOP:
                    self.move_top(board, dt)
                case Moves.MOVE_BOTTOM:
                    self.move_bottom(board, dt)
                case Moves.MOVE_LEFT:
                    self.move_left(board, dt)
                case Moves.MOVE_RIGHT:
                    self.move_right(board, dt)
                case _:
                    pass
            self.movesTaken = self.movesTaken + 1
            i = 0