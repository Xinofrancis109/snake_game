import turtle as t


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def increasescore(self):
        self.score += 1

        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))