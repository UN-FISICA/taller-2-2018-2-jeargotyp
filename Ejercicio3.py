
# coding: utf-8

# In[ ]:

#Numero 3
import turtle
import msvcrt
from turtle import *
setup(450, 500, 0, 0)
screensize(500, 500)
l1=input("Numero de lados del poligono: ")
lados=int(l1)
l2=input("Numero de lados del poligono alineacion: ")
l22=int(l2)
angle = 360 / lados
angulo=360/l22

for i in range(l22):
    penup()
    forward(150)
    pendown()
    turtle.left(angulo)
  
    for k in range(lados):
        
        turtle.fd(40)
        turtle.left(angle)
    #forward(150)
    #turtle.right(angulo-2*d)   
    #turtle.right(360-angulo)    
   
turtle.done()
msvcrt.getch()


# In[11]:




# In[ ]:



