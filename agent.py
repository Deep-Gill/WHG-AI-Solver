import pygame


class Agent:

    def __init__(self, x, y, width=30, height=30, speed=300, colour="red2"):
        self.__dimensions = pygame.Vector2(width, height)
        self.__SPEED = speed
        self.__COLOUR = colour
        self.__x = x
        self.__y = y
        self.__position = pygame.Vector2(x, y)
        self.__body = pygame.Rect(self.__position, self.__dimensions)

    def draw(self, screen):
        pygame.draw.rect(screen, self.__COLOUR, self.get_body())

    def __update_position(self):
        self.__position = pygame.Vector2(self.__x, self.__y)

    def is_inside_board(self, board, x, y):
        newBody = pygame.Rect(pygame.Vector2(x, y), self.__dimensions)
        return board.contains(newBody)

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
        self.__update_position()

    def move_top(self, board, dt):
        newPosY = self.__y - (self.__SPEED * dt)
        self.__y = newPosY if self.is_inside_board(
            board, self.__x, newPosY) else self.__y

    def move_bottom(self, board, dt):
        newPosY = self.__y + (self.__SPEED * dt)
        self.__y = newPosY if self.is_inside_board(
            board, self.__x, newPosY) else self.__y

    def move_left(self, board, dt):
        newPosX = self.__x - (self.__SPEED * dt)
        self.__x = newPosX if self.is_inside_board(
            board, newPosX, self.__y) else self.__x

    def move_right(self, board, dt):
        newPosX = self.__x + (self.__SPEED * dt)
        self.__x = newPosX if self.is_inside_board(
            board, newPosX, self.__y) else self.__x

    def get_position(self):
        return self.__position

    def get_dimensions(self):
        return self.__dimensions

    def get_body(self):
        return pygame.Rect(self.__position, self.__dimensions)
