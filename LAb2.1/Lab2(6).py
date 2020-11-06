import turtle

#Упражнение 6
turtle.shape('turtle')
n = input()
n = int(n)
for i in range(1,n):
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(360/n)
