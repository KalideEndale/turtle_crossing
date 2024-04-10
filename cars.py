from turtle import Turtle
import random

CAR_POSITION = 180
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
X_POS = 300

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManger(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)



    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def reset_car(self):
        self.Y_POS = random.randint(-260, 280)
        self.goto(x=X_POS, y=self.Y_POS)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT