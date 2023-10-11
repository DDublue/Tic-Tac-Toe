### tictactoe.py
### Tic-tac-toe program

# -----

import pygame, sys
from game import Game
from pygame.locals import *

def main():
    pygame.font.init()
    g = Game()
    g.run()

if __name__ == "__main__":
    main()
    