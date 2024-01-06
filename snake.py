import time as tm
from turtle import Turtle
points = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.c_snake()
        self.head = self.segments[0]

    def c_snake(self):
        for i in points:
            self.add_segment(i)

    def add_segment(self, i):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.goto(i)
        self.segments.append(new_snake)

    def increase(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        tm.sleep(0.1)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


