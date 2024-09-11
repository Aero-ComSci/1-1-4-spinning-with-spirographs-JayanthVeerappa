import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
colors = ['red', 'green', 'blue', 'black', 'orange', 'purple', 'pink', 'brown']
size = 20
size_incrm = 10 
go = True
while go == False:  # this is a Zero iteration loop, it will never run because go is set to True, but it needs go to be false to run
#This is also an infinite loop, because it will run forever  as long as go is false 
    

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


wn = trtl.Screen()
wn.mainloop()
