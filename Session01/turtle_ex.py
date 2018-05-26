from turtle import *

x = int(input("Nhap so canh:"))
y = 360 // x
speed(-1)
shape("turtle")
color("green")
fillcolor("red")

#Vuông 1
# begin_fill()

for i in range(x):
    forward(100)
    left(y)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(7)

# end_fill()

# #Vuông 2
# color("orange")
# left(30)
# begin_fill()
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# end_fill()

# left(30)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)

mainloop()
