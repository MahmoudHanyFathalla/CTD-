import turtle
screen=turtle.Screen()
trtl=turtle.Turtle()
screen.setup(620,620)
screen.bgcolor('black')
trtl.pensize(4)
trtl.shape('turtle')
trtl.penup()
trtl.pencolor('red')
m=0
for i in range(12):
      m=m+1
      trtl.penup()
      trtl.setheading(-30*i+60)
      trtl.forward(150)
      trtl.pendown()
      trtl.forward(25)
      trtl.penup()
      trtl.forward(20)
      trtl.write(str(m),align="center",font=("Arial", 12, "normal"))
      if m==12:
        m=0
      trtl.home()
trtl.home()
trtl.setpos(0,-250)
trtl.pendown()
trtl.pensize(10)
trtl.pencolor('blue')
trtl.circle(250)
trtl.penup()
trtl.setpos(0,0)
trtl.pendown()
trtl.pencolor('olive')
trtl.ht()

trtl.setposition(0, 0)
trtl.speed(100)
trtl.pencolor('green')
for i in range(120):
    trtl.forward(80)
    
    trtl.penup()
    trtl.setposition(0, 0)
    trtl.pendown()
    
    trtl.right(3)
trtl.pencolor('blue')
for i in range(360):
    trtl.forward(60)
    
    trtl.penup()
    trtl.setposition(0, 0)
    trtl.pendown()
    
    trtl.right(1)
       
turtle.done()