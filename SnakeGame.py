import time
import random
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = 0
scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)

def update_score():
    scoreboard.clear()
    scoreboard.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 20, "normal")
    )

update_score()

food = Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.8, 0.8)

food.goto(random.randint(-280, 280),
    random.randint(-280, 280))

startPos = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in startPos:
    newSegment = Turtle("square")
    newSegment.color("white")
    newSegment.penup()
    newSegment.goto(position)
    segments.append(newSegment)

head = segments[0]

def up():
    if head.heading() != 270:
        head.setheading(90)

def down():
    if head.heading() != 90:
        head.setheading(270)

def left():
    if head.heading() != 0:
        head.setheading(180)

def right():
    if head.heading() != 180:
        head.setheading(0)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

game = True

while game:
    screen.update()
    time.sleep(0.1)
    for segnum in range(len(segments)-1, 0, -1):
        newx = segments[segnum-1].xcor()
        newy = segments[segnum-1].ycor()
        segments[segnum].goto(newx, newy)

    head.forward(20)


    if head.distance(food) < 15:
        food.goto(
            random.randint(-280, 280),
            random.randint(-280, 280)
        )

        score += 1
        update_score()

        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()

        last_segment = segments[-1]
        new_segment.goto(
            last_segment.xcor(),
            last_segment.ycor())

        segments.append(new_segment)

    if (
        head.xcor() > 290 or
        head.xcor() < -290 or
        head.ycor() > 290 or
        head.ycor() < -290
    ):
        game = False

        scoreboard.goto(0, 0)
        scoreboard.write(
            "GAME OVER",
            align="center",
            font=("Arial", 24, "bold")
        )

    for segment in segments[1:]:
        if head.distance(segment) < 10:
            game = False
            scoreboard.goto(0, 0)
            scoreboard.write(
                "GAME OVER",
                align="center",
                font=("Arial", 24, "bold"))

screen.exitonclick()