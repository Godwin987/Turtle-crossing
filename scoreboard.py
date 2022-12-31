from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.goto(-230, 270)
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.hideturtle()
        self.clear()
        self.write(f"Level: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.score += 1
