from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("blank")
        self.goto(0, 265)
        self.color("white")
        self.score = -1
        with open("data.txt", mode="r") as h_score:
            self.high_score = h_score.read()
        self.show_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as h_score:
                h_score.write(f"{self.high_score}")
        self.score = -1

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)
