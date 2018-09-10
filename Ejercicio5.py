
# coding: utf-8

# In[3]:

#numero 5
import turtle
from turtle import *
setup(450, 500, 0, 0)
screensize(500, 500)

lineas1=input("Numero de filas de la piramide: ")
lineas=int(lineas1)
lados=lineas+2
d=0
hideturtle()
angulo = 360 / lados
#angl1 = 360 / lados
for n in range(0,lineas):
    penup()
    goto(30*d+d,60*d)
    pendown()
    for j in range(n,lineas):
        penup()
        forward(60)
        pendown()
        #turtle.left(90)
        angulo = 360 / lados
        for k in range(lados):
            turtle.fd(30)
            turtle.lt(angulo)
    lados-=1
    d+=1
    
turtle.done()


# In[ ]:



