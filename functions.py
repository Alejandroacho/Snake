import pygame

from models import *
from settings import *

def initialize_game():
    pygame.init()
    game = Game()
    return game

def get_initial_items():
    screen_measures = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_measures)
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()    
    return screen, clock

def get_fonts():
    font_style = get_font_style()
    score_font = get_score_font_style()
    return font_style, score_font

def get_font_style():
    font_style = pygame.font.SysFont("bahnschrift", 25)
    return font_style

def get_score_font_style():
    score_font = pygame.font.SysFont("bahnschrift", 35)
    return score_font

def print_score(score, screen):
    score_font = get_score_font_style()
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    screen.blit(value, [0, 0])
    pygame.display.update()

def message(msg, color, screen):
    font_style = pygame.font.SysFont("bahnschrift", 25)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

def lose_screen(screen, play_game, snake_length, game):
    print_lose_screen(screen, snake_length)
    for event in pygame.event.get():
        if event.type == KEY_PRESSED:
            key = event.key
            if key == Q:
                game.over = True
                game.close = False
            if key == C:
                game.close = False
                play_game()

def print_lose_screen(screen, snake_length):
    fill_screen(screen, BLACK)
    message("You Lost! Press C to play again or Q to quit", RED, screen)
    score = snake_length - 1
    print_score(score, screen)
    pygame.display.update()

def fill_screen(screen, color):
    screen.fill(color)

def quit_game():
    pygame.quit()
    quit()