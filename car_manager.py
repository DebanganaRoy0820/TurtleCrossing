import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            x_pos = 300
            y_pos = random.randint(-230, 230)
            new_car.goto(x_pos, y_pos)
            new_car.speed("slowest")
            self.all_cars.append(new_car)


    def refresh(self):
        for car in self.all_cars:
            x_pos = car.xcor() - self.speed
            y_pos = car.ycor()
            car.goto(x_pos, y_pos)
            
    def increase_car_speed(self):
        self.speed += MOVE_INCREMENT
