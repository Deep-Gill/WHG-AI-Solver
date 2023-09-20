import pygame

class Bullets:
    def __init__(self):
        pass


class Bullet(pygame.sprite.Sprite):

    SB_DIAMETER = 20
    RADIUS = SB_DIAMETER/2
    BB_DIAMETER = 3.5*SB_DIAMETER # Big Bullet Diameter
    RIGHT_EDGE = 845
    LEFT_EDGE = 60
    TOP_EDGE = 120
    BOTTOM_EDGE = 500
    SB_SPEED = 2 # Small Bullet Speed
    BB_SPEED = 4 # Big Bullet Speed
    SMALLBULLET_Y1 = 490 # Initial y position for bottom half of small bullet
    SMALLBULLET_Y2 = 130 # Initial y position for top half of small bullet

    # Store all bullet params

    BULLETS = [(65,  SMALLBULLET_Y1, 0, SB_SPEED,  0, -1, SB_DIAMETER),
               (155, SMALLBULLET_Y1, 0, SB_SPEED,  0, -1, SB_DIAMETER),
               (245, SMALLBULLET_Y1, 0, SB_SPEED,  0, -1, SB_DIAMETER),
               (335, SMALLBULLET_Y1, 0, SB_SPEED,  0, -1, SB_DIAMETER),
               (425, SMALLBULLET_Y1, 0, SB_SPEED,  0, -1, SB_DIAMETER),
               (515, SMALLBULLET_Y1, 0, SB_SPEED,  0, -1, SB_DIAMETER),
               (605, SMALLBULLET_Y1, 0, SB_SPEED,  0, -1, SB_DIAMETER),
               (695, SMALLBULLET_Y1, 0, SB_SPEED,  0, -1, SB_DIAMETER),
               (785, SMALLBULLET_Y1, 0, SB_SPEED,  0, -1, SB_DIAMETER),
               (110, SMALLBULLET_Y2, 0, SB_SPEED,  0, 1,  SB_DIAMETER), 
               (200, SMALLBULLET_Y2, 0, SB_SPEED,  0, 1,  SB_DIAMETER), 
               (290, SMALLBULLET_Y2, 0, SB_SPEED,  0, 1,  SB_DIAMETER),
               (380, SMALLBULLET_Y2, 0, SB_SPEED,  0, 1,  SB_DIAMETER),
               (470, SMALLBULLET_Y2, 0, SB_SPEED,  0, 1,  SB_DIAMETER),
               (560, SMALLBULLET_Y2, 0, SB_SPEED,  0, 1,  SB_DIAMETER),
               (650, SMALLBULLET_Y2, 0, SB_SPEED,  0, 1,  SB_DIAMETER),
               (740, SMALLBULLET_Y2, 0, SB_SPEED,  0, 1,  SB_DIAMETER),
               (830, SMALLBULLET_Y2, 0, SB_SPEED,  0, 1,  SB_DIAMETER),
               
               (245,   307.5, BB_SPEED, 0,  1,  0, 2*SB_DIAMETER),
               (87.5,  150,   BB_SPEED, 0,  1,  1, BB_DIAMETER),
               (807.5, 465,   BB_SPEED, 0, -1, -1, BB_DIAMETER),
               (180,   240,   BB_SPEED, 0,  1,  1, BB_DIAMETER),
               (715,   375,   BB_SPEED, 0, -1, -1, BB_DIAMETER)]

    def __init__(self, pos_x, pos_y, speed_x, speed_y, dir_x, dir_y, diameter=SB_DIAMETER):
        super().__init__()

        self.diameter = diameter
        self.radius = diameter/2
        self.image = pygame.Surface((self.diameter, self.diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0, 255), (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.direction_x = dir_x
        self.direction_y = dir_y
    

    def in_middle(self):
        if (self.rect.centerx >= 177.5 and self.rect.centerx <= 717.5) and (
            self.rect.centery >= 240 and self.rect.centery <= 375):
            return True
        else:
            return False
        
    def handle_sb(self):
        if self.rect.bottom >= self.BOTTOM_EDGE or self.rect.top <= self.TOP_EDGE:
            self.direction_y *= -1
          

    def handle_central_bullet(self):
        if self.rect.right >= 660 or self.rect.left <= 220:
            self.direction_x *= -1

    def handle_bb(self):
        if self.in_middle():
            self.handle_bb_inner_cases()
        else:
            self.handle_bb_outer_cases()


    def bb_go_down(self):
        self.speed_x = 0
        self.direction_x *= -1
        self.speed_y = self.BB_SPEED

    def bb_go_left(self):
        self.speed_y = 0
        self.direction_y *= -1
        self.speed_x = self.BB_SPEED

    def bb_go_up(self):
        self.speed_x = 0
        self.direction_x *= -1
        self.speed_y = self.BB_SPEED

    def bb_go_right(self):
        self.speed_y = 0
        self.direction_y *= -1
        self.speed_x = self.BB_SPEED


    def handle_bb_inner_cases(self):
        if self.speed_x > 0:
            if self.direction_x == 1 and self.rect.centerx >= 715:
                self.bb_go_down()
            elif self.direction_x == -1 and self.rect.centerx <= 180:
                self.bb_go_up()

        if self.speed_y > 0:
            if self.direction_y == 1 and self.rect.centery >= 370:
                self.bb_go_left()
            elif self.direction_y == -1 and self.rect.centery <= 245:
                self.bb_go_right()

    def handle_bb_outer_cases(self):
        if self.speed_x > 0:
            if self.direction_x == 1 and self.rect.right >= self.RIGHT_EDGE:
                self.bb_go_down()
            elif self.direction_x == -1 and self.rect.left <= self.LEFT_EDGE:
                self.bb_go_up()

        if self.speed_y > 0:
            if self.direction_y == 1 and self.rect.bottom >= self.BOTTOM_EDGE:
                self.bb_go_left()
            elif self.direction_y == -1 and self.rect.top <= self.TOP_EDGE:
                self.bb_go_right()

    def update(self):
        self.rect.x += self.speed_x * self.direction_x
        self.rect.y += self.speed_y * self.direction_y

        if self.diameter == self.SB_DIAMETER:
            self.handle_sb()

        elif self.diameter == 2*self.SB_DIAMETER:
            self.handle_central_bullet()

        elif self.diameter == self.BB_DIAMETER:
            self.handle_bb()

                
    def create_bullets(cls, bullet_params = BULLETS):
        bullets = pygame.sprite.Group()
        for para in bullet_params:
            bullet = cls(para[0], para[1], para[2], para[3], 
                         para[4], para[5], para[6])
            bullets.add(bullet)
        return bullets
        
        

