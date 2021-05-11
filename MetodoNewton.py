#Modulo: MetodoNewton.py import MetodoNewton as MN
#Implementacion del metodo de Newton para sistemas de ecuaciones no lienales.
#Autor: Alexis Tercero (@math.by.uri) 
#Exitoso

import numpy as np
import math

#implementacion de norma del supremo
def norma(Y):
  '''Y: numpy.ndarray'''
  delta = np.abs(Y)
  return max(delta)

def VFormat(X):
  '''
  X: numpy.ndarray
  '''
  if X.size == 4:
    return '({:.6f},{:.6f},{:.6f},{:.6f})'.format(*X)
  if X.size == 3:
    return '({:.6f},{:.6f},{:.6f})'.format(*X)
  if X.size == 2:
    return '({:.6f},{:.6f})'.format(*X)

def NewtonNL(Xk,F,J,N=30,T=1e-6):
  '''
  Parametros:
    Xk: numpy.ndarray.
    F: function. Sietema No lienal F(X).
    J: function. Matriz Jacobiana de F como funcion J(X).
    N: int. Numero maximo de iteraciones, 30 por defecto.
    T: float. Tolerancia al error, 1e-6 por defecto.

  Retorna la solucion del sistema F: 
    X: numpy.ndarray 

  Errores: 
    El metodo no funciona si el rango de Xk,F y J no son iguales.

  Funciones utilizadas de otras librerias:
    np.linalg.solve(a, b)
    Solve a linear matrix equation, or system of linear scalar equations.

    Computes the “exact” solution, x, of the well-determined, i.e., full rank, linear matrix equation ax = b.

    Parameters
    a(…, M, M) array_like
    Coefficient matrix.

    b{(…, M,), (…, M, K)}, array_like
    Ordinate or “dependent variable” values.

    Returns
    x{(…, M,), (…, M, K)} ndarray
    Solution to the system a x = b. Returned shape is identical to b.

    Raises
    LinAlgError
    If a is singular or not square.
  '''
  print('Metodo de Newton para sistemas no lienales')
  print('punto inicial x0:',Xk)
  #paso 1
  k = 1
  #paso 2
  while k <= N:
    #paso 3
    FX = F(*Xk)
    JX = J(*Xk)
    #paso 4: Resuelva el sistema J(X)Y = -F(x)
    #La funcion np.linalg.solve resuelve el sitema lineal de la forma AX=B
    Y = np.linalg.solve(JX,-FX)
    #paso 5
    Xk = Xk + Y
    #paso 6
    #se presentan datos resultados por iteracion
    delta = norma(Y)
    print('punto X{}:'.format(k),list(Xk) , 'error: ', delta)
    if delta < T:
      print('\n\nLa solucion es:',VFormat(Xk))#crear funcion FormatoVector
      return Xk
    #paso 7
    k += 1
  else: print('No se llego a la sulucion en {} iteraciones.'.format(N))
