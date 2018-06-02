from turtle import *

shape("turtle")
speed(-1)
color("blue")

for i in range(36):
    for j in range(4):
        forward(50)
        left(90)
    left(10)

mainloop()