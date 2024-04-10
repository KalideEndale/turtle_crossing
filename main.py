
from turtle import Turtle, Screen
from players import Players
from cars import CarManger
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("white")
screen.title("Turtle crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Players()

car = CarManger()

scoreboard = Scoreboard((0,280))

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True

while game_is_on:
    time.sleep(player.move_speed)
    screen.update()

    car.create_car()
    car.move()

    #Detect collision with car
    for a_car in car.all_cars:
        if a_car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

        if player.is_at_finish_line():
            scoreboard.increase_level()
            player.reset_position()
            car.level_up()











screen.exitonclick()