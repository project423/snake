from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("blue")
        self.penup()
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)
    
    def move(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)
