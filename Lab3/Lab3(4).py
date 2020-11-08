import turtle
import math
from random import randint

Numb_of_trtls = 50
stps_of_time_Numb = 1000

turtle.color('blue')
turtle.width(4)
turtle.speed(100000000)
turtle.penup()
turtle.goto(-350, -350)
turtle.pendown()
turtle.goto(-350, 350)
turtle.goto(350, 350)
turtle.goto(350, -350)
turtle.goto(-350, -350)

angl=[]

pool = [turtle.Turtle(shape='turtle') for i in range(Numb_of_trtls)]


for unit in pool:
        unit.penup()
        unit.speed(900)
        unit.goto(randint(-330,330), randint(-330,330))

for i in range(Numb_of_trtls):
        angl.append(randint(10,360))


j = 0
for unit in pool:
    unit.left(angl[j])
    j += 1

    
for i in range(stps_of_time_Numb):
        k = 0
        for unit in pool:
            unit.forward(6)
            if ((unit.xcor() <= -330) or (unit.xcor() >= 330) or
                (unit.ycor() <= -330) or (unit.ycor() >= 330)):
                unit.left(180 - 2*angl[k])
            elif (unit.xcor() == unit.ycor()) and ((unit.xcor() == 330) or
                                               (unit.xcor() == -330)):
                unit.left(180)
        k += 1
