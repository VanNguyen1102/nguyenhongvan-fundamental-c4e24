from turtle import *

shape("turtle")

d = 0

for i in range(40):
    forward(d)
    left(90)
    d += 10

mainloop()