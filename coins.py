import pygame


class Coin(pygame.sprite.Sprite):

    '''
    Implement Coins Blocks
    A coin block is, as the name suggests, a block of coins positioned closeby to each other.
    They are defined relative to the position of the centermost coin as called the reference coin.
    Level 30 has four coin blocks: Top Left (TL), Top Right (TR), Bottom Right (BR), Board Center (C).
    We implement, explicity, the coin positions for each block and append them onto coin map for Level 30.
    '''
    TOTAL = 46
    # Coin Spacing
    COIN_SP = 22.5
    
    # Coin Block: Top Left (TL)
    # Position of reference coin
    TL_MID_X = 87.5
    TL_MID_Y = 150

    # Define positions for Top Left Coin Block
    COIN_MAP_TL = [(TL_MID_X-COIN_SP, TL_MID_Y-COIN_SP), (TL_MID_X, TL_MID_Y-COIN_SP), (TL_MID_X+COIN_SP, TL_MID_Y-COIN_SP),
                   (TL_MID_X-COIN_SP,  TL_MID_Y),        (TL_MID_X, TL_MID_Y),         (TL_MID_X+COIN_SP,  TL_MID_Y),
                   (TL_MID_X-COIN_SP, TL_MID_Y+COIN_SP), (TL_MID_X, TL_MID_Y+COIN_SP), (TL_MID_X+COIN_SP, TL_MID_Y+COIN_SP)]
    
    
    # Coin Block: Top Right (TR)
    # Position of reference coin
    TR_MID_X = 807.5
    TR_MID_Y = 150
    # Define positions for Top Right Coin Block
    COIN_MAP_TR = [(TR_MID_X-COIN_SP, TR_MID_Y-COIN_SP), (TR_MID_X, TR_MID_Y-COIN_SP), (TR_MID_X+COIN_SP, TR_MID_Y-COIN_SP),
                   (TR_MID_X-COIN_SP,  TR_MID_Y),        (TR_MID_X, TR_MID_Y),         (TR_MID_X+COIN_SP,  TR_MID_Y),
                   (TR_MID_X-COIN_SP, TR_MID_Y+COIN_SP), (TR_MID_X, TR_MID_Y+COIN_SP), (TR_MID_X+COIN_SP, TR_MID_Y+COIN_SP)]
    
    
    # Coin Block: Bottom Right (BR)
    # Position of reference coin
    BR_MID_X = 807.5
    BR_MID_Y = 465
    # Define positions for Bottom Right Coin Block
    COIN_MAP_BR = [(BR_MID_X-COIN_SP, BR_MID_Y-COIN_SP), (BR_MID_X, BR_MID_Y-COIN_SP), (BR_MID_X+COIN_SP, BR_MID_Y-COIN_SP),
                   (BR_MID_X-COIN_SP,  BR_MID_Y),        (BR_MID_X, BR_MID_Y),         (BR_MID_X+COIN_SP,  BR_MID_Y),
                   (BR_MID_X-COIN_SP, BR_MID_Y+COIN_SP), (BR_MID_X, BR_MID_Y+COIN_SP), (BR_MID_X+COIN_SP, BR_MID_Y+COIN_SP)]

    # Coin Block: Central (C) 
    # Position of reference coin
    C_MID_X = 447.5
    C_MID_Y = 307.5
    # Define positions for Centermost Coin Block
    COIN_MAP_C = [(C_MID_X-COIN_SP*9, C_MID_Y), (C_MID_X-COIN_SP*8, C_MID_Y), (C_MID_X-COIN_SP*7, C_MID_Y), 
                  (C_MID_X-COIN_SP*6, C_MID_Y), (C_MID_X-COIN_SP*5, C_MID_Y), (C_MID_X-COIN_SP*4, C_MID_Y), 
                  (C_MID_X-COIN_SP*3, C_MID_Y), (C_MID_X-COIN_SP*2, C_MID_Y), (C_MID_X-COIN_SP*1, C_MID_Y), 
                  (C_MID_X, C_MID_Y), 
                  (C_MID_X+COIN_SP*1, C_MID_Y), (C_MID_X+COIN_SP*2, C_MID_Y), (C_MID_X+COIN_SP*3, C_MID_Y), 
                  (C_MID_X+COIN_SP*4, C_MID_Y), (C_MID_X+COIN_SP*5, C_MID_Y), (C_MID_X+COIN_SP*6, C_MID_Y), 
                  (C_MID_X+COIN_SP*7, C_MID_Y), (C_MID_X+COIN_SP*8, C_MID_Y), (C_MID_X+COIN_SP*9, C_MID_Y)]


    COIN_MAP_L30 = COIN_MAP_TL + COIN_MAP_TR + COIN_MAP_BR + COIN_MAP_C


    def __init__(self, pos_x, pos_y, coin_diameter=15):
        super().__init__()
        self.COIN_DIAMETER = coin_diameter
        self.COIN_RADIUS = coin_diameter/2
        self.image = pygame.Surface((self.COIN_DIAMETER, self.COIN_DIAMETER), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (212, 175, 55, 255), (self.COIN_RADIUS, self.COIN_RADIUS), self.COIN_RADIUS) 
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        pass

    def create_coins(cls, positions = COIN_MAP_L30):
        coins = pygame.sprite.Group()
        for pos in positions:
            coin = cls(pos[0], pos[1])
            coins.add(coin)
        return coins       
        return coins       
