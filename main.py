from turtle import Screen
from snake import Snake
from score_board import ScoreBoard
from food import Food


import time

delay = 0.1

wn = Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)

#Accesses the X on the GUI
canvas = wn.getcanvas()
root = canvas.winfo_toplevel()
#Snake 
snake = Snake()

#Food
food = Food()

#Score Board
scoreboard = ScoreBoard()



#Turn off the screen updates
wn.tracer(0)

#Keyboard bindings
wn.listen()
wn.onkeypress(snake.go_up, "Up")
wn.onkeypress(snake.go_down, "Down")
wn.onkeypress(snake.go_left, "Left")
wn.onkeypress(snake.go_right, "Right")

segments = []

def game_reset():
    snake.reset()
    scoreboard.reset()
    food.move()


def on_close():
    global game_is_on
    game_is_on = False

#Terminal does now throw a lot of erros when the x is clicked
root.protocol("WM_DELETE_WINDOW", on_close)


#Main game loop
game_is_on = True
while game_is_on:
    wn.update()

    #Check for a collision with the border
    if snake.xcor()> 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        game_reset()
        

    #Check for collision with the food
    if snake.distance(food) < 20:
        #Move the food to a random spot on the screen
        food.move()
        #Add a segment
        snake.add_segment()
        #Add one to score
        scoreboard.add_one()     
        
    #Move the end segments first in reverse order
    snake.add_segments()


    snake.move()
    #Check if snake collides with itslef
    for segments in snake.segments:
        if snake.distance(segments) < 20:
            game_reset()
    time.sleep(delay)

