import os
os.chdir(os.path.dirname(os.path.dirname(__file__)))
from agent import Agent
from coins import Coin
import random

class AgentGA(Agent):
    def __init__(self):
        super().__init__()
        self.coins = Coin.create_coins(Coin)
        self.isAlive = True
        
    def move(self, board, dt):
        moveInt = random.randint(0, 4)
        if not self.isAlive: moveInt = 0
        match moveInt:
            case 1:
                self.move_top(board, dt)
            case 2:
                self.move_bottom(board, dt)
            case 3:
                self.move_left(board, dt)
            case 4:
                self.move_right(board, dt)
            case _:
                pass