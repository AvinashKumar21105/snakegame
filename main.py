import random
import time
from turtle import Turtle, Screen
d = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.c = []
        self.snake()
        self.head = self.c[0]

    def snake(self):
        for i in range(3):
            a = Turtle()
            a.color("white")
            a.shape("square")
            a.penup()
            a.backward(20 * i)
            self.c.append(a)

    def grow(self):
        a = Turtle()
        a.color("white")
        a.shape("square")
        a.penup()
        a.goto(self.c[-1].xcor(), self.c[-1].ycor())
        self.c.append(a)

    def move(self):
        for j in range(len(self.c) - 1, 0, -1):
            x = self.c[j - 1].xcor()
            y = self.c[j - 1].ycor()
            self.c[j].goto(x, y)
        self.c[0].fd(d)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def reset(self):
        for i in self.c:
            i.goto(10000,10000)
        self.c.clear()
        self.snake()
        self.head = self.c[0]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("high.txt")as high:
            self.high_score=int(high.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()


    def update(self):
        self.clear()
        self.write(f"score:{self.score},High score:{self.high_score}", move=False, align="center", font=("Arial", 15, "normal"))

    def high(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high.txt",mode="w") as high:
                high.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def increase(self):
        self.score += 1
        self.update()

    def over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER,Final score:{self.score}", move=False, align="center", font=("Arial", 15, "normal"))


b = Screen()
b.tracer(0)
b.setup(width=600, height=600)
b.bgcolor("black")
b.title("Snake Babu")

snake = Snake()
food = Food()
score = Score()

b.listen()
b.onkey(fun=snake.up, key="Up")
b.onkey(fun=snake.down, key="Down")
b.onkey(fun=snake.left, key="Left")
b.onkey(fun=snake.right, key="Right")

end = False
while not end:
    b.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_food()
        score.increase()
        snake.grow()
    if snake.head.xcor() > 280 or snake.head.ycor() > 300 or snake.head.xcor() < -295 or snake.head.ycor() < -295:
        score.high()
        snake.reset()

    for i in snake.c[1:]:
        if snake.head.distance(i) < 15:
            score.high()
            snake.reset()

b.exitonclick()