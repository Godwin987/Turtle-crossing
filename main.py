import time
from turtle import Screen
import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = ScoreBoard()

screen.onkey(player.move, "Up")

count = 0
loop_delay = 6
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.forward_move()

    if count > loop_delay:
        car.random_cars()
        count = 0
    count += 1

    for cars in car.car_list:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 290:
        player.goto(0, -280)
        car.speed_increment(car_manager.MOVE_INCREMENT)
        scoreboard.update_score()
        loop_delay *= 0.7


screen.exitonclick()
