import pygame


class Board:

    def __init__(self):
        pass


class BoardL30(Board):

    LEVEL = 30

    SQUARE_SIZE = 45
    DIMENSIONS = pygame.Vector2(18 * SQUARE_SIZE, 9 * SQUARE_SIZE)
    POSITION = pygame.Vector2(45, 105)
    SAFETY_DIMENSIONS = pygame.Vector2(2 * SQUARE_SIZE, 2 * SQUARE_SIZE)
    SAFETY_POSITION = pygame.Vector2(45, 510)
    BACKGROUND_COLOUR = "salmon"
    OUTLINE_COLOUR = "black"
    OUTLINE_DIMENSIONS = pygame.Vector2(
        (18 * SQUARE_SIZE) + 10, (9 * SQUARE_SIZE) + 10)
    OUTLINE_POSITION = pygame.Vector2(40, 100)

    def __init__(self):
        super().__init__()
        self.__body = pygame.Rect(self.POSITION, self.DIMENSIONS)

    def draw(self, display):
        self.draw_outline(display)
        pygame.draw.rect(display, "white", pygame.Rect(
            self.POSITION, self.DIMENSIONS))
        pygame.draw.rect(display, "green", pygame.Rect(
            self.SAFETY_POSITION, self.SAFETY_DIMENSIONS))

    def draw_outline(self, display):
        pygame.draw.rect(display, self.OUTLINE_COLOUR, pygame.Rect(
            self.OUTLINE_POSITION, self.OUTLINE_DIMENSIONS))

    def get_body(self):
        return self.__body
