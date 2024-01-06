import turtle as t
from scoreboard import ScoreBoard
from snake_food import Food
from snake import Snake

screen = t.Screen()
screen.setup(width=800, height=600)
screen.getcanvas()
screen.tracer(0)
snake = Snake()
scoreboard = ScoreBoard()
food = Food()
screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
score = 0
start = True
while start:
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase()
        scoreboard.clear()
        scoreboard.increasescore()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380:
        start = False
        scoreboard.goto(-80, 0)
        scoreboard.write("Game Over", font=("Arial", 24, "normal"))

    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        start = False
        scoreboard.goto(-80, 0)
        scoreboard.write("Game Over", font=("Arial", 24, "normal"))
    screen.update()

    for i in snake.segments[1:-1]:
        if snake.head.distance(i) < 10:
            start = False
            scoreboard.goto(-80, 0)
            scoreboard.write("Game Over", font=("Arial", 24, "normal"))


screen.exitonclick()
