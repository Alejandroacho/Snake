import pygame

from functions import *
from models import *
from settings import *

game = initialize_game()
screen, clock = get_initial_items()

def play_game():
    food = Food()
    snake = Snake()
    while not game.over:
        # Lose screen
        while game.close == True:
            lose_screen(screen, play_game, snake.length, game)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                game.over = True
            if event.type == KEY_PRESSED:
                key = event.key
                if key in MOVEMENTS:
                    snake.define_movement(key)

        # Refresh screen
        fill_screen(screen, BLUE)

        # Check snake movements and draw snake/food
        snake.check_if_went_out(game)
        food.draw(screen)
        snake.move()
        snake.check_self_bit(game)
        snake.draw(screen)
        snake.check_if_ate_food(food)

        # Update score
        score = game.get_score(snake)
        print_score(score, screen)

        clock.tick(SNAKE_SPEED)

    quit_game()

play_game()
