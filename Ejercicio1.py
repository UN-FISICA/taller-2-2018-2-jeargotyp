
# coding: utf-8

# In[ ]:

import turtle
from turtle import *

setup(450, 500, 0, 0)
screensize(500, 500)

lados=4

angle = 360 / lados
penup()
goto(100, 0)
pendown()
for i in range(lados):
    turtle.fd(50)
    turtle.lt(angle)
    
for i in range(lados):
    turtle.fd(50)
    turtle.lt(angle)
penup()
goto(100, 100)
pendown()
for i in range(lados):
    turtle.fd(50)
    turtle.lt(angle)
penup()
goto(0, 100)
pendown()
for i in range(lados):
    turtle.fd(50)
    turtle.lt(angle)
penup()
goto(0, 0)
pendown()
for i in range(lados):
    turtle.fd(50)
    turtle.lt(angle)

    

turtle.done()

