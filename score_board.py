from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("high_score.txt", mode="r") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            with open("high_score.txt", mode="w") as data:
                self.high_score = 0
                data.write("0")
            
        self.speed(0)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_one(self):
        self.score +=1
        self.set_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", mode="w") as data:
            data.write(f"{self.high_score}")
    
    def reset(self):
        self.score = 0
        self.update_score()