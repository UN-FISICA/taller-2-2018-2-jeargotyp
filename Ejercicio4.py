
# coding: utf-8

# In[3]:

#Numero 4
import turtle
from turtle import *
setup(450, 500, 0, 0)
screensize(500, 500)
lados1=input("Numero de lados del poligono: ")
lados=int(lados1)
lineas1=input("Numero de filas de la piramide: ")
lineas=int(lineas1)


d=0
hideturtle()
angulo = 360 / lados

for n in range(0,lineas):
    penup()
    goto(20*d+d,40*d)
    pendown()
    for j in range(n,lineas):
        penup()
        forward(40)
        pendown()
        #turtle.left(90)
        for k in range(lados):
            turtle.fd(30)
            turtle.lt(angulo)
    d+=1  
    
turtle.done()


# In[ ]:



