import turtle as tr


def nan(n,x) :
    a = 360/n
    for i in range(0,n) :
        tr.forward(x)
        tr.left(a)

for i in range(1,10) :
    nan(4,i * 20)
    tr.penup()
    tr.backward(10)
    tr.left(-90)
    tr.forward(10)
    tr.left (90)
    tr.pendown()
    
