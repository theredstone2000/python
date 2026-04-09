import turtle
import math
import operator
from tkinter import simpledialog
a = simpledialog.askfloat(None, "a for ax + b")
b = simpledialog.askfloat(None, "b for ax + b")
turtle.screensize(500,500)
turtle.goto(0,0)
turtle.dot(8,"red")
turtle.sety(turtle.ycor()+b)

turtle.setheading(math.degrees(math.atan(a)))
turtle.forward(500)
turtle.backward(1000)
turtle.mainloop()