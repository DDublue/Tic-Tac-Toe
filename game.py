### game.py
### Game class for tictactoe.py

# -----

import pygame, sys
from random import choice
from board import Board
from player import Player
from pygame import *

# colors
WHITE  = (255,255,255)
RED    = (255,  0,  0)
YELLOW = (255,255,  0)
GREEN  = (  0,255,  0)
BLUE   = (  0,  0,255)
BLACK  = (  0,  0,  0)
LGRAY  = (237,237,237)

class Game:
    BG = WHITE
    ALPHA = 255
    DIFF = 20
    
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        self.WIDTH = 600
        self.HEIGHT = 800
        self.BOARD_SIZE = self.WIDTH - self.DIFF
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 30)
        self.board = Board((self.WIDTH-self.BOARD_SIZE)//2, (self.WIDTH-self.BOARD_SIZE)//2, self.BOARD_SIZE, self.BOARD_SIZE)
        self.p1 = Player("Player 1", 1)
        self.p2 = Player("Player 2", 0)
        self.turn = self.firstturn = choice([self.p1, self.p2])
        self.game_active = True
        self.winner = -1
        self.mouse_pos = [0,0]
        self.lmb_clicked = False
        
    def draw(self) -> None:
        self.screen.fill(self.BG)
        self.board.draw(self.screen)
        self.screen.blit(self.font.render(f"Player 1's score: {self.p1.score}", True, BLACK), (50, self.BOARD_SIZE + 90))
        self.screen.blit(self.font.render(f"Player 2's score: {self.p2.score}", True, BLACK), (self.WIDTH - 225, self.BOARD_SIZE + 90))
        if self.winner == -1:
            self.screen.blit(self.font.render(f"{self.turn.name}'s turn", True, BLACK), (self.WIDTH//2-70, self.BOARD_SIZE + 50))
        else:
            self.screen.blit(self.font.render(f"Press R to play again", True, BLACK), (self.WIDTH//2-100, self.BOARD_SIZE + 140))
            if self.winner == 2:
                self.screen.blit(self.font.render(f"Draw", True, BLACK), (self.BOARD_SIZE//2-10, self.BOARD_SIZE + 50))
            else:
                self.screen.blit(self.font.render(f"Winner: {self.turn.name}", True, BLACK), (self.WIDTH//2-80, self.BOARD_SIZE + 50))
        
    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_r and not self.game_active:
                    self.restart()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.game_active:
                        self.mouse_pos = pygame.mouse.get_pos()
                        self.lmb_clicked = True
                    
    def run(self) -> None:
        self.restart()
        while self.running:
            self.check_events()
            
            if self.game_active:
                if self.lmb_clicked:
                    self.lmb_clicked = False
                    i, j = self.check_sq_clicked(self.mouse_pos)
                    if i == j and i == -1:
                        pass
                    elif self.board.board[i][j] == -1:
                        self.board.update(self.turn.pos, i, j)
                        self.check_winner()
                        self.check_draw()
                        if self.winner == -1:
                            self.change_player()
                
                if self.winner == 2:
                    self.game_active = False        
                elif self.winner != -1:
                    self.game_active = False
                    if self.winner:
                        self.p1.update_score()
                    else:
                        self.p2.update_score()
                        
            self.draw()
            pygame.display.update()
            self.clock.tick(60)
            
        # end_while
        pygame.quit()
        sys.exit()
    
    def restart(self):
        self.board.clear()
        self.winner = -1
        self.game_active = True
        self.firstturn = self.p2 if self.firstturn.get_pos() else self.p1 # bug
        self.change_player()
    
    def check_sq_clicked(self, mouse_pos):
        if self.board.x + 3 < mouse_pos[0] and mouse_pos[0] < self.board.x + self.board.sq_sz:
            if self.board.y + 3 < mouse_pos[1] and mouse_pos[1] < self.board.y + self.board.sq_sz: # box (0,0)
                return (0,0)
            elif self.board.y + self.board.sq_sz < mouse_pos[1] and mouse_pos[1] < self.board.y + self.board.sq_sz*2: # box (1,0)
                return (1,0)
            elif self.board.y + self.board.sq_sz*2 < mouse_pos[1] and mouse_pos[1] < self.board.y + self.board.sq_sz*3: # box (2,0)
                return (2,0)
        elif self.board.x + self.board.sq_sz < mouse_pos[0] and mouse_pos[0] < self.board.x + self.board.sq_sz*2:
            if self.board.y + 3 < mouse_pos[1] and mouse_pos[1] < self.board.y + self.board.sq_sz: # box (0,1)
                return (0,1)
            elif self.board.y + self.board.sq_sz < mouse_pos[1] and mouse_pos[1] < self.board.y + self.board.sq_sz*2: # box (1,1)
                return (1,1)
            elif self.board.y + self.board.sq_sz*2 < mouse_pos[1] and mouse_pos[1] < self.board.y + self.board.sq_sz*3: # box (2,1)
                return (2,1)
        elif self.board.x + self.board.sq_sz*2 < mouse_pos[0] and mouse_pos[0] < self.board.x + self.board.sq_sz*3:
            if self.board.y + 3 < mouse_pos[1] and mouse_pos[1] < self.board.y + self.board.sq_sz: # box (0,2)
                return (0,2)
            elif self.board.y + self.board.sq_sz < mouse_pos[1] and mouse_pos[1] < self.board.y + self.board.sq_sz*2: # box (1,2)
                return (1,2)
            elif self.board.y + self.board.sq_sz*2 < mouse_pos[1] and mouse_pos[1] < self.board.y + self.board.sq_sz*3: # box (2,2)
                return (2,2)
        else:
            return (-1,-1)
    
    def check_winner(self):
        if self.board.board[0][0] == self.board.board[0][1] == self.board.board[0][2] != -1:
            self.winner = self.board.board[0][0]
        elif self.board.board[1][0] == self.board.board[1][1] == self.board.board[1][2] != -1:
            self.winner = self.board.board[1][0]
        elif self.board.board[2][0] == self.board.board[2][1] == self.board.board[2][2] != -1:
            self.winner = self.board.board[2][0]
        elif self.board.board[0][0] == self.board.board[1][0] == self.board.board[2][0] != -1:
            self.winner = self.board.board[0][0]
        elif self.board.board[0][1] == self.board.board[1][1] == self.board.board[2][1]!= -1:
            self.winner = self.board.board[0][1]
        elif self.board.board[0][2] == self.board.board[1][2] == self.board.board[2][2]!= -1:
            self.winner = self.board.board[0][2]
        elif self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2]!= -1:
            self.winner = self.board.board[0][0]
        elif self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0]!= -1:
            self.winner = self.board.board[0][2]
        else:
            self.winner = -1
    
    def check_draw(self):
        if all(self.board.board[i][j] != -1 for i in range(3) for j in range(3)) and self.winner == -1:
            self.winner = 2
    
    def change_player(self):
        self.turn = self.p2 if self.turn.pos else self.p1
