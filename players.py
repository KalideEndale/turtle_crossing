from turtle import Turtle
MOVING_DISTANCE = 20
TURTLE_DIRECTION = 90
STARTING_POSITION = (0,-280)
FINISH_LINE_Y = 280

class Players(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(TURTLE_DIRECTION)
        self.reset_position()
        self.move_speed = 0.1


    def move(self):
        self.forward(MOVING_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False