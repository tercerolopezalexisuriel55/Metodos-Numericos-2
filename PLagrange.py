# Interpolacion de Lagrange
# divisoresL solo para mostrar valores
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from math import  *

def PLagrange(xi,fi,fun):
  # PROCEDIMIENTO
  # Polinomio de Lagrange
  n = len(xi)
  x = sym.Symbol('x')
  polinomio = 0
  divisorL = np.zeros(n, dtype = float)
  for i in range(0,n,1):
      # Termino de Lagrange
      numerador = 1
      denominador = 1
      for j  in range(0,n,1):
          if (j!=i):
              numerador = numerador*(x-xi[j])
              denominador = denominador*(xi[i]-xi[j])
      terminoLi = numerador/denominador

      polinomio = polinomio + terminoLi*fi[i]
      divisorL[i] = denominador

  # simplifica el polinomio
  polisimple = polinomio.expand()

  # SALIDA
  print('    valores de fi: ',fi)
  print('divisores en L(i): ',divisorL)
  print()
  print('Polinomio de Lagrange, expresiones')
  print(polinomio)
  print()
  print('Polinomio de Lagrange: ')
  print(polisimple)

  # retorna Polinomio resultante
  return sym.lambdify(x,polisimple)