import turtle as tr

tr.shape('turtle')
tr.speed(3)
def nan(n,x) :
    a = 360/n
    for i in range(0,n) :
        tr.forward(x)
        tr.left(a)

for i in range(10,360) :
    tr.forward(1/20/3.14 * i)
    tr.left(5)


