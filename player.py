from turtle import Turtle
STARTING_POSITION = (0, -265)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 265


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0,-265)

    def move(self):
      new_x = self.xcor()
      new_y = self.ycor()
      self.goto(new_x, new_y)
      self.forward(MOVE_DISTANCE)

    def collision(self,car_manager):
        game_is_on = True
        for car in car_manager.all_cars:
            if car.distance(self) < 20:
                game_is_on = False
        return game_is_on

    def next_level(self):
        if self.distance(0,FINISH_LINE_Y) < 5:
            return True