from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_pos()

    def reset_pos(self):
        '''Returns turtle to the starting position'''
        self.goto(STARTING_POSITION)

    def move(self):
        '''Move the turtle upwords'''
        self.fd(MOVE_DISTANCE)

    def is_at_finish_line(self):
        '''Returns true if the turtle is at the finish line'''
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        