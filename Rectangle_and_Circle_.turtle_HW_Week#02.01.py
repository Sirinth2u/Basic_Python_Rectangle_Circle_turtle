import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Rectangle():
    for i in range(4):
        tao.forward(100)
        tao.left(90)
        
Rectangle()
tao.clear()

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
   
Go(100,50)
Go(-40,70)
Rectangle()
Go(25,50)
Rectangle()

tao1 = turtle.Pen()
tao1.shape('turtle')


for x in range(30):
    tao1.circle(25)
    tao1.left(20)
