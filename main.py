from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My own snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        for circle in snake.circles:
            circle.color(food.randomcolor)
        food.refresh()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        replay = screen.textinput('Game Over!', 'Play again?: Y or N').lower()
        if replay == 'n':
            game_is_on = False
        # elif replay == 'y':
        #     score.reset()
        #     snake.reset()
        snake.reset()
        score.reset()
    for circle in snake.circles[4:]:
        if snake.head.distance(circle) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
