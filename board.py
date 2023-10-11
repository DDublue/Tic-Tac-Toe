### board.py
### Board class for tictactoe

# -----

import pygame
from pygame.locals import *

# colors
WHITE  = (255,255,255)
RED    = (255,  0,  0)
YELLOW = (255,255,  0)
GREEN  = (  0,255,  0)
BLUE   = (  0,  0,255)
BLACK  = (  0,  0,  0)
LGRAY  = (237,237,237)

class Board:
    ALPHA = 255
    RATIO = 13/15
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sq_sz = width//3
        self.fix = (self.sq_sz - self.sq_sz*self.RATIO)//2
        self.board = self.create_board()
        self.surf = pygame.Surface((self.width, self.height))
        self.X_img = pygame.transform.scale(pygame.image.load("data/images/X.png").convert_alpha(), (self.sq_sz*self.RATIO, self.sq_sz*self.RATIO))
        self.O_img = pygame.transform.scale(pygame.image.load("data/images/O.png").convert_alpha(), (self.sq_sz*self.RATIO, self.sq_sz*self.RATIO))
        self.X_img.set_alpha(self.ALPHA)
        self.O_img.set_alpha(self.ALPHA)
    
    def __repr__(self):
        return str(self.board)
    
    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))
        self.surf.fill(LGRAY)
        self.draw_board_lines()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 1:
                    self.surf.blit(self.X_img, (self.fix + j * self.sq_sz, self.fix + i * self.sq_sz))
                elif self.board[i][j] == 0:
                    self.surf.blit(self.O_img, (self.fix + j * self.sq_sz, self.fix + i * self.sq_sz))
    
    def draw_board_lines(self):
        pygame.draw.line(self.surf, BLACK, (0, 0), (0, self.height), 7)
        pygame.draw.line(self.surf, BLACK, (self.sq_sz, 0), (self.sq_sz, self.height), 5)
        pygame.draw.line(self.surf, BLACK, (self.sq_sz*2,0), (self.sq_sz*2, self.height), 5)
        pygame.draw.line(self.surf, BLACK, (self.sq_sz*3,0), (self.sq_sz*3, self.height), 7)
        pygame.draw.line(self.surf, BLACK, (0, 0), (self.width, 0), 7)
        pygame.draw.line(self.surf, BLACK, (0, self.sq_sz), (self.width, self.sq_sz), 5)
        pygame.draw.line(self.surf, BLACK, (0, self.sq_sz*2), (self.width, self.sq_sz*2), 5)
        pygame.draw.line(self.surf, BLACK, (0, self.sq_sz*3), (self.width, self.sq_sz*3), 7)
    
    def create_board(self):
        return [[-1 for _ in range(3)] for _ in range(3)]
    
    def update(self, player, i, j):
        self.board[i][j] = player
    
    def clear(self):
        self.board = self.create_board()
        