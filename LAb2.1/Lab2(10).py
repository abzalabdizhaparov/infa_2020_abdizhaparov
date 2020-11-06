import turtle as tr

#Упражнение 10
def nan(n,x) :
    a = 360/n
    for i in range(0,n) :
        tr.left(a)
        tr.forward(x)
tr.speed(10)
for i in range(36,360,12) :
    nan(100,5)
    tr.left(i)
        
