#Autor: Alexis Uriel Tercero Lopez
#Metodo de Broyden Pregunta 2 Examen
import MetodoBroyden as MB
import numpy as np
import math

def F(x,y,w): #sistema
  f1 = 25*x + y**2 - 4*w -13
  f2 = x**2 + 10*y - w -88
  f3 = y**3 - 25*w + 22
  return np.array([f1,f2,f3])

def J(x,y,w): #matriz jacobiana de F
  c1 = [15, 2*y, -4]
  c2 = [2*x, 10, -1]
  c3 = [0, 3*y**2, - 25]
  return np.array([c1,c2,c3])

X0 = np.array([-10,-10,-10])#punto inicial
a = MB.Broyden(X0,F,J,T=1e-06)#La mada al metodo
MB.VFormat(F(*a))
