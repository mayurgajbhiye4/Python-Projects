from tkinter import *
import random

# global variables
GAME_WIDTH = 1000 
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = '##00FF00'
FOOD_COLOUR = '#FF0000'
BACKGROUND_COLOUR = '#000000'


class Snake:
    pass

class Food:
    def __init__(self):
        x = random.randint(0, ((GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE)
        y = random.randint(0, ((GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE)

def next_turn(self):
    pass

def change_direction(self):
    pass

def game_over(self):
    pass

window = Tk()
window.title("Snake game")
window.resizable(True, True)

snake = Snake()
food = Food()

C = Canvas(window,width= GAME_WIDTH, height= GAME_HEIGHT)
window.mainloop()




