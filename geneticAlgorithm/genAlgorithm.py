import os
os.chdir(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from math import ceil, pow, sqrt
from random import randint
import pygame
from geneticAlgorithm.agentga import AgentGA

class GeneticAlgorithm:
    CROSSOVER_RATE = 0.75
    MAX_MUTATION_RATE = 0.01
    SELECTION_RATE = 0.01
    DEATH_PENALTY = 0
    
    def __init__(self):
        pass
    
    def initializeGenerationZero(self, agents=None, moves=None, path=None):
        if path is None and agents is not None and moves is not None:
            for agent in agents:
                agent.moves = self.generateRandomMoves(moves)
        elif path is not None:
            pass
        else:
            raise Exception('Wrong set of arguments to initializeGenerationZero')
    
    def initializeNextGeneration(self, agents, numOfAgents):
        topAgents = self.selectFittest(agents)
        return self.crossover(topAgents, numOfAgents)
    
    def crossover(self, fittestAgents, population):
        newGeneration = pygame.sprite.Group()
        for i in range(population):
            childAgent = AgentGA()
            parentAgentIndex = randint(0, len(fittestAgents) - 1)
            parentAgent = fittestAgents[parentAgentIndex]
            retainedMoves = ceil(self.CROSSOVER_RATE * parentAgent.movesTaken)
            newMoves = self.generateRandomMoves(len(parentAgent.moves) - retainedMoves)
            childMoves = parentAgent.moves[:retainedMoves] + newMoves
            childAgent.moves = childMoves
            self.mutation(childAgent, parentAgent.movesTaken)
            newGeneration.add(childAgent)
        return newGeneration

    def mutation(self, agent, movesTaken):
        retainedMoves = ceil(self.CROSSOVER_RATE * movesTaken)
        mutations = ceil(self.MAX_MUTATION_RATE * retainedMoves)
        mutations = randint(1, mutations)
        for i in range(mutations):
            mutatedMove = randint(0, retainedMoves - 1)
            newMove = randint(0, 4)
            agent.moves[mutatedMove] = newMove

    def selectFittest(self, agents):
        for agent in agents: 
            self.fitnessScore(agent)
        fittestAgents = sorted(agents, key=lambda agent: agent.fitnessScore, reverse=True)
        selectNum = ceil(self.SELECTION_RATE * len(fittestAgents))
        return fittestAgents[:selectNum]

    def fitnessScore(self, agent):
        coinsScore = pow(agent.coinsCaught + 1, 3)
        displacementScore = sqrt(pow(agent.rect.x - agent.INITIAL_POSITION.x, 2) + 
                                 pow(agent.rect.y - agent.INITIAL_POSITION.y, 2))
        displacementScore = displacementScore / agent.movesTaken
        deathScore = 1 - self.DEATH_PENALTY
        agent.fitnessScore =  deathScore * displacementScore * coinsScore
        
    def generateRandomMoves(self, movesNum):
        moves = []
        for i in range(movesNum):
            randomMove = randint(0, 4)
            moves.append(randomMove)
        return moves