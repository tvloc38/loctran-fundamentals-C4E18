from turtle import *

c = ["red", "blue", "brown", "yellow", "grey"]

for i in range(3,8):
    color(c[i-3])
    for j in range(i):
        forward(50)
        left(360/i)

mainloop()