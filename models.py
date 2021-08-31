import pygame
import random

from settings import *

class Game():
    def __init__(self):
        self.over = False
        self.close = False
    
    def get_score(self, snake):
        score = snake.length - 1
        return score

class Snake():
    def __init__(self):
        self.body = []
        self.x = SNAKE_INITIAL_X
        self.y = SNAKE_INITIAL_Y
        self.x_change = 0
        self.y_change = 0
        self.length = SNAKE_INITIAL_LENGTH
        self.body = []
        self.head = []
        self.last_movement = None
    
    def draw(self, screen):
        for block in self.body:
            snake_configuration = [block[0], block[1], BLOCK, BLOCK]
            pygame.draw.rect(screen, BLACK, snake_configuration)
    
    def define_movement(self, key):
        if key == LEFT and self.last_movement != RIGHT:
            self.move_left()
        elif key == RIGHT and self.last_movement != LEFT:
            self.move_right()
        elif key == UP and self.last_movement != DOWN:
            self.move_up()
        elif key == DOWN and self.last_movement != UP:
            self.move_down()

    def move_left(self):
        self.last_movement = LEFT
        self.x_change = -BLOCK
        self.y_change = 0

    def move_right(self):
        self.last_movement = RIGHT
        self.x_change = BLOCK
        self.y_change = 0
        
    def move_up(self):
        self.last_movement = UP
        self.y_change = -BLOCK
        self.x_change = 0

    def move_down(self):
        self.last_movement = DOWN
        self.y_change = BLOCK
        self.x_change = 0

    def move(self):
        self.head = []
        self.x += self.x_change
        self.y += self.y_change
        self.head.append(self.x)
        self.head.append(self.y)
        self.body.append(self.head)
        if len(self.body) > self.length:
            del self.body[0]
    
    def check_if_went_out(self, game):
        quit_by_width = self.x >= SCREEN_WIDTH or self.x < 0
        quit_by_height = self.y >= SCREEN_HEIGHT or self.y < 0
        if quit_by_width or quit_by_height:
            game.close = True
    
    def check_self_bit(self, game):
        for block in self.body[:-1]:
            if block == self.head:
                game.close = True
    
    def check_if_ate_food(self, food):
        if self.x == food.x and self.y == food.y:
            food.reappear()
            self.length += 1

class Food():
    def __init__(self):
        self.x = self.get_random_x()
        self.y = self.get_random_y()
    
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, [self.x, self.y, BLOCK, BLOCK])

    def get_random_x(self):
        random_range = random.randrange(0, SCREEN_WIDTH - BLOCK) / 10.0
        food_x = round(random_range) * 10.0
        return food_x
    
    def get_random_y(self):
        random_range = random.randrange(0, SCREEN_HEIGHT - BLOCK) / 10.0
        food_y = round(random_range) * 10.0
        return food_y
    
    def reappear(self):
        self.x = self.get_random_x()
        self.y = self.get_random_y()