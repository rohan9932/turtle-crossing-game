from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        '''Shows the level of the player'''
        self.goto(-220, 260)
        self.write(arg= f"Level: {self.score}", move= True, align= ALIGNMENT, font= FONT)

    def update(self):
        '''Updates the scoreboard'''
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        '''Prints Game over if player crashes with a car'''
        self.home()
        self.write(arg= "GAME OVER!", move= True, align= ALIGNMENT, font= FONT)
        