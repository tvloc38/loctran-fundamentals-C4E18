from turtle import *

for i in range(3,7,1):
    if i % 2 == 0:
        color("red")
    else:
        color("green")
    for j in range(i):
        forward(50)
        left(360/i)

mainloop()