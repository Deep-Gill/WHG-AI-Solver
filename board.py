import pygame


class Board(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass


class BoardL30(Board):

    LEVEL = 30

    SQUARE_SIZE = 45
    DIMENSIONS = pygame.Vector2(18 * SQUARE_SIZE, 11 * SQUARE_SIZE) # MAY NEED TO KEEP AS 9 instead of 11
    POSITION = pygame.Vector2(45, 105)
    GOAL_DIMENSIONS = pygame.Vector2(2 * SQUARE_SIZE, 2 * SQUARE_SIZE)
    GOAL_POSITION = pygame.Vector2(45, 510)
    BACKGROUND_COLOUR = "salmon"
    OUTLINE_COLOUR = "black"
    OUTLINE_DIMENSIONS = pygame.Vector2((18 * SQUARE_SIZE) + 10, (11 * SQUARE_SIZE) + 10) # MAY NEED TO KEEP AS 9 instead of 11
    OUTLINE_POSITION = pygame.Vector2(42, 102) # Original 40, 100

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/WHG_L30_Board_810_495.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=self.POSITION)
        self.mask = pygame.mask.from_surface(self.image)
        self.outlineImage = pygame.image.load('images/WHG_L30_Board_B.png')
        self.outlineImage = pygame.transform.scale(self.outlineImage, self.OUTLINE_DIMENSIONS)
        self.outlineRect = self.outlineImage.get_rect(topleft=self.OUTLINE_POSITION)
        goalMaskImage = pygame.Surface(self.GOAL_DIMENSIONS, pygame.SRCALPHA)
        self.goalMask = pygame.mask.from_surface(goalMaskImage)
        self.goalRect = goalMaskImage.get_rect(topleft=self.GOAL_POSITION)

    def draw(self, display):
        self.draw_outline(display)
        display.blit(self.image, self.rect)

    def draw_outline(self, display):
        display.blit(self.outlineImage, self.outlineRect)
        
    def is_inside(self, objectMask, objectRect, objectMaskBits):
        offsetX = objectRect.x - self.rect.x
        offsetY = objectRect.y - self.rect.y
        overlapBits = self.mask.overlap_area(objectMask, (offsetX, offsetY))
        return overlapBits == objectMaskBits
    
    def is_inside_goal(self, objectMask, objectRect, objectMaskBits):
        offsetX = objectRect.x - self.goalRect.x
        offsetY = objectRect.y - self.goalRect.y
        overlapBits = self.goalMask.overlap_area(objectMask, (offsetX, offsetY))
        return overlapBits == objectMaskBits




