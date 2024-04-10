from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.level = 1
        # self.score = 0
        self.color("black")
        self.penup()
        self.goto(position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write( self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
)