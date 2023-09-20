import pygame


class Agent(pygame.sprite.Sprite):

    __INITIAL_POSITION = pygame.Vector2(90, 555)
    __DIMENSIONS = pygame.Vector2(30, 30)
    __SPEED = 300
    __COLOUR = "red2"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(self.__DIMENSIONS, pygame.SRCALPHA)
        self.image.fill(self.__COLOUR)
        self.rect = self.image.get_rect(center=self.__INITIAL_POSITION)
        self.mask = pygame.mask.from_surface(self.image)
        self.__maskBits = self.mask.count()
        self.coinsCaught = 0
        self.fails = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def user_move(self, board, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move_top(board, dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move_bottom(board, dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.move_left(board, dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move_right(board, dt)

    def move_top(self, board, dt):
        rect_copy = self.rect.copy()
        rect_copy.y = self.rect.y - (self.__SPEED * dt)
        if board.is_inside(self.mask, rect_copy, self.__maskBits):
            self.rect = rect_copy

    def move_bottom(self, board, dt):
        rect_copy = self.rect.copy()
        rect_copy.y = self.rect.y + (self.__SPEED * dt)
        if board.is_inside(self.mask, rect_copy, self.__maskBits):
            self.rect = rect_copy

    def move_left(self, board, dt):
        rect_copy = self.rect.copy()
        rect_copy.x = self.rect.x - (self.__SPEED * dt)
        if board.is_inside(self.mask, rect_copy, self.__maskBits):
            self.rect = rect_copy

    def move_right(self, board, dt):
        rect_copy = self.rect.copy()
        rect_copy.x = self.rect.x + (self.__SPEED * dt)
        if board.is_inside(self.mask, rect_copy, self.__maskBits):
            self.rect = rect_copy