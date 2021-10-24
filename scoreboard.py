from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(0, 235)
        self.hideturtle()
        self.color("Black")
        self.write(f"Level:{self.level}", align=ALIGNMENT, font=FONT)

    def display_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level:{self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
