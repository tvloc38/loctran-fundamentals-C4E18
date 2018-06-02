from turtle import *

shape("turtle")
speed(-1)
color("blue")

for i in range(1,100,2):
    for j in range(4):
        forward(i)
        left(90)
    left(10)

mainloop()