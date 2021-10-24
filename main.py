import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
i = 0
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(player.move, "Up")
    car_manager.create_car()
    car_manager.refresh()
    game_is_on = player.collision(car_manager)
    if game_is_on is False:
        scoreboard.game_over()
    level_up = player.next_level()
    if level_up:
        scoreboard.display_level()
        car_manager.increase_car_speed()
        player.goto(0, -265)

screen.exitonclick()
