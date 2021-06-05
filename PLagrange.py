#Modulo: PLagrange.py import import PLagrange as PL
#Implementacion del polinomio interpolante (de grado n) 
#de lagrange para n+1 puntos.
#Autor: Alexis Tercero (@math.by.uri) 
#Exitoso
import numpy as np
import sympy as sym

def Lnk(n,k,xi,x, show=False):
  ''' Termino de Lagrange
  L_{n,k}(x)=\Pi_{i=0 \\ i\neq k}^n \frac{(x-x_i)}{(x_k-x_i)}
  n: int: numero de puntos
  k: int: punto de refereocia
  xi: list: conjunto de puntos muestra
  show=False: Boolean: muestra o no datos detallados del proceso'''
  numerador = 1
  denominador = 1
  for i  in range(n):
    if (i!=k):
      numerador = numerador*(x-xi[i])
      denominador = denominador*(xi[k]-xi[i])
  if show:
    print('L_{}'.format(k),'=')
    print(numerador)
    print('-'*35)
    print(denominador,'\n')
  return numerador/denominador
  
def PLagrange(xi,fi,show=False):
  '''Polinomio de lagrange
  Parametros------------------------------------------------------
  P(x)=\sum_{k=0}^n f(x_k)L_{n,k}(x)
  xi: list: conjunto de puntos muestra
  fi: list: valores mapeados de f en xi
  show=False: Boolean: muestra o no datos detallados del proceso
  ----------------------------------------------------------------
  Retorna una funcion lambda Polinomio P(x)
  '''
  print('valores de fi: ',fi)
  print('valores de xi: ',xi)
  # PROCEDIMIENTO
  # Polinomio de Lagrange
  n = len(xi)# numero de puntos 
  x = sym.Symbol('x') #expresamos la variable 
  polinomio = 0

  for k in range(n):#generacion del polinomio interpolante
    terminoLk = Lnk(n,k,xi,x,show)
    polinomio = polinomio + terminoLk*fi[k]

  # simplifica el polinomio
  polisimple = polinomio.expand()
  
  if show:
    print()
    print('Polinomio de Lagrange, expresiones')
    print(polinomio)
  print()
  print('Polinomio de Lagrange: ')
  print(polisimple)

  # retorna Polinomio resultante
  return sym.lambdify(x,polisimple)
