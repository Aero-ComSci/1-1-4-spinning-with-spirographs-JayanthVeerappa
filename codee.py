import turtle as trtl
import random

painter = trtl.Turtle()

screen = trtl.Screen()
screen.setup(width=800, height=800)

painter.speed(0)

colors = ['red', 'green', 'blue', 'black', 'orange', 'purple', 'pink', 'brown']
size = 20
size_incrm = 10 

for _ in range(50):  
    painter.penup()
    painter.goto(-size / 2, -size / 2)  
    painter.pendown()
    
    color = random.choice(colors)
    painter.color(color) 
    
    painter.color()
    for _ in range(4):
        painter.forward(size)
        painter.left(90)

    
    size += size_incrm

screen.mainloop()
