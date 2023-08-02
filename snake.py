from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.circles = []
        self.create_snake()
        self.head = self.circles[0]

    def create_snake(self):
        for pos in POSITIONS:
            new_circle = Turtle("circle")
            new_circle.color("white")
            new_circle.penup()
            new_circle.goto(pos)
            self.circles.append(new_circle)

    def reset(self):
        for circle in self.circles:
            circle.goto(1000, 1000)
        self.circles.clear()
        self.create_snake()
        self.head = self.circles[0]

    def extend(self):
        new_circle = Turtle("circle")
        new_circle.color("white")
        new_circle.penup()
        new_circle.goto(self.circles[-1].position())
        self.circles.append(new_circle)

    def move(self):
        for i in range(len(self.circles) - 1, 0, -1):
            new_xcor = self.circles[i - 1].xcor()
            new_ycor = self.circles[i - 1].ycor()
            self.circles[i].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
