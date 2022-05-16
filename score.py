from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("Courier", 75, "bold"))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("Courier", 75, "bold"))

    def add_to_an_r(self):
        self.r_score += 1
        self.update_score_board()

    def add_to_an_l(self):
        self.l_score += 1
        self.update_score_board()



