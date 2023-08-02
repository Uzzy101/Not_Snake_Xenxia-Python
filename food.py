from turtle import Turtle
import random

COLORS = ["white", "green", "violet", "blue", "red", "orange", "purple", "cyan"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.randomcolor = random.choice(COLORS)
        self.color(self.randomcolor)
        self.penup()
        self.shapesize(0.5, 0.5)
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)

    def refresh(self):
        self.randomcolor = random.choice(COLORS)
        self.color(self.randomcolor)
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)
