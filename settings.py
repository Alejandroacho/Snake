import pygame

# Game settings
GAME_OVER = False
GAME_CLOSE = False
BLOCK = 10

# Movements
QUIT = pygame.QUIT
UP = pygame.K_UP
DOWN = pygame.K_DOWN
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
KEY_PRESSED = pygame.KEYDOWN
Q = pygame.K_q
C = pygame.K_c
MOVEMENTS = [UP, DOWN, LEFT, RIGHT]

# Colors settings
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (255, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Snake settings
SNAKE_SPEED = 15
SNAKE_INITIAL_X = SCREEN_WIDTH / 2
SNAKE_INITIAL_Y = SCREEN_HEIGHT / 2
SNAKE_INITIAL_LENGTH = 1
