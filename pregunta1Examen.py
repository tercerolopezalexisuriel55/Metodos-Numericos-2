#Autor: Alexis Uriel Tercero Lopez 419084338
#Metodo de Newton Pregunta 1 Examen
import MetodoNewton as MN 
import numpy as np
import math

def F(x,y,w,z): #sistema
  f1 = 4*x - y + w -x*z
  f2 = -x + 3*y - 2*w - y*z
  f3 = x - 2*y + 3*w - w*z
  f4 = x**2 + y**2 + w**2 - 8
  return np.array([f1,f2,f3,f4])

def J(x,y,w,z): #matriz jacobiana de F
  r1 = [4-z, -1, 1, -x]
  r2 = [-1, 3-z, -2, -y]
  r3 = [1, -2, 3, -w]
  r4 = [2*x, 2*y, 2*w, 0]
  return np.array([r1,r2,r3,r4])

X0 = np.array([1,1,1,1])#punto inicial

a = MN.NewtonNL(X0,F,J,T=1e-06)#Llamada al metodo
MN.VFormat(F(*a))
