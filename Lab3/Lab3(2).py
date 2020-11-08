import turtle
import math

turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()

def Numb(a: str):
    angl1 = 45
    forwd1 = 100*math.sqrt(2)
    angl2 = -135
    forwd2 = 200
    angl3  = -90
    forwd3 = 100
    angl4 = 180
    n = []
    
    Numb = ( [0, forwd3, angl3, forwd2, angl3, forwd3, angl3, forwd2,
              angl3, forwd3, angl3, forwd2, 0, 0, 0, 0, 0, 0], 
             [angl1, forwd1, angl2, forwd2, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0], 
             [0, forwd3, angl3, forwd3, -angl1, forwd1, -angl2, forwd3, 
             0, 0, 0, 0, 0, 0, 0, angl3, 0, 0], 
             [0, forwd3, angl2, forwd1, -angl2, forwd3, angl2, forwd1,
             0, 0, 0, 0, 0, 0, 0, -angl2, forwd3, angl3], 
             [angl3, forwd3, -angl3, forwd3, angl4, forwd2, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0],
             [0, forwd3, angl4, forwd3, -angl3, forwd3, -angl3, forwd3,
             angl3, forwd3, angl3, forwd3, 0, 0, 0, angl4, forwd3, angl3], 
             [angl2, forwd1, angl1, forwd3, -angl3, forwd3, -angl3, forwd3, 
             -angl3, forwd3, -angl3, forwd3, -angl3, forwd3, 0, angl3, 0,
             0,],
             [0, forwd3, angl2, forwd1, angl1, forwd3, 0, 0, 0, 0, 0, 0, 0,
             0, 0, -angl3, forwd3, angl3],
             [angl3, forwd2, -angl3, forwd3, -angl3, forwd3, -angl3, forwd3,
             angl3, forwd3, angl3, forwd3, angl3, forwd2, 0, 0, 0, 0,], 
             [0, forwd3, angl3, forwd3, angl3, forwd3, angl3, forwd3, angl3,
             forwd3, angl3, forwd3, -angl1, forwd1, 0, -angl2, forwd3, angl3])
    
    for i in range(len(a)):
        n.append(int(a[i]))
        print(n)
        
    for i in range(len(a)):
        j = 0
        k = n[i]
        if n[i] == 1:
            turtle.penup()
            turtle.left(angl3)
            turtle.forward(forwd3)
            turtle.right(angl3)
            turtle.pendown()
        elif n[i] == 6:
            turtle.penup()
            turtle.forward(forwd3)
            turtle.pendown()
        while j<13:
            turtle.left(Numb[k][j])
            j += 1
            turtle.forward(Numb[k][j])
            j += 1
        turtle.penup()
        while j<18:
            turtle.forward(Numb[n[i]][j])
            j += 1
            turtle.left(Numb[n[i]][j])
            j += 1
            
        turtle.backward(200)
        turtle.left(90)
        turtle.forward(30)
        turtle.pendown()
        
a = input()
Numb(a)

