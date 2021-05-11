#pregunta 3 Examen Alexis Uriel Tercero Lopez
#Alexis Tercero
import numpy as np
from math import  *
import PLagrange as PL

# INGRESO , Datos de prueba
def fun(x):
  return log2(x)

xi = np.array([1, 1.5, 2])
fi = np.array([fun(x) for x in xi])
P = PL.PLagrange(xi,fi,fun)
print('\nP(0.45) = {:.6}'.format(P(0.45)))
