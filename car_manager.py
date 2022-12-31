from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.random_cars()
        self.faster = STARTING_MOVE_DISTANCE

    def random_cars(self):
        cars = Turtle()
        cars.shape("square")
        cars.shapesize(stretch_wid=1, stretch_len=2)
        cars.color(random.choice(COLORS))
        cars.penup()
        cars.setheading(180)
        cars.goto(300, random.randint(-250, 250))
        self.car_list.append(cars)

    def forward_move(self):
        for car in self.car_list:
            car.forward(self.faster)

    def speed_increment(self, increase):
        self.faster += increase
