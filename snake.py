from  turtle import Turtle
import time


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.direction = "stop"
        self.segments = []

    def move(self):
        if self.direction == "up":
            y = self.ycor()
            self.sety(y + 20)

        if self.direction == "down":
            y = self.ycor()
            self.sety(y - 20)

        if self.direction == "right":
            x = self.xcor()
            self.setx(x + 20)

        if self.direction == "left":
            x = self.xcor()
            self.setx(x - 20)
        
    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"
    
    def add_segment(self):
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)

    def add_segments(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)

        if len(self.segments) > 0:
            x = self.xcor()
            y = self.ycor()
            self.segments[0].goto(x,y)

    def reset(self):
        time.sleep(1)
        self.goto(0,0)
        self.direction = "stop"
        #Hide the segments
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        



