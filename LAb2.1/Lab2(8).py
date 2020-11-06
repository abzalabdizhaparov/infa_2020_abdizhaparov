
import turtle

turtle.shape('turtle')

turtle.speed(10)

rotations_number = 10
step = 20
length = step
for i in range(2*rotations_number):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    length += step

