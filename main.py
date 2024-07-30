# In this project the famuous crossing game is created with turtle graphics
# TODO: Create a turtle player which starts at the botton of the screen and move upwords while clicking up arrow.
# TODO: Create cars. 50 px from up and down are safe areas for the player
# TODO: Detect collision of the turtle with the car and stop the game if happens
# TODO: Detect the player's reaching on the finish line 
# TODO: Create a scoreboard

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setting up the main screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Rohan's Turtle Crossing Game")
screen.bgcolor("PeachPuff")
screen.tracer(0)

# Creating a player
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Setting up the controls
screen.listen()
screen.onkey(fun=player.move, key="Up")

# Main game engine
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating and moving the cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collsion with the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False # finishes the game
            scoreboard.game_over() # prints game over

    # Detect collision with the finish line
    if player.is_at_finish_line():
        player.reset_pos() 
        car_manager.level_up()
        scoreboard.update()

    
screen.exitonclick()
