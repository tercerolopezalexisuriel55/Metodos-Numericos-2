# -*- coding: utf-8 -*-
#modulo integracion de romberg RombergInt.py 
#import RombergInt as RI
import numpy

def romberg( f, a, b, n ):
  """Estima la integral de f(x) en [a,b] usando la Integracion de Romberg.
  uso:
      r = romberg( f, a, b, n )

  entrada:
      f       - funcion a integrar,
      [a, b]  - intervalo de integracion,
      n       - para R_{n,n} nivel de recursion

  salida:
      numpy float array - tabla de valores
  """
  #paso1
  r = numpy.array( [[0] * (n+1)] * (n+1), float )
  h = b - a
  #paso2
  r[0,0] = 0.5 * h * ( f( a ) + f( b ) )
  #paso 3
  powerOf2 = 1
  for i in range( 1, n + 1 ):#paso8
    #Paso 4 (aproximacion metodo del trapécio)
    h = 0.5 * h #paso7
    sum = 0.0
    powerOf2 = 2 * powerOf2
    for k in range( 1, powerOf2, 2 ):
      sum = sum + f( a + k * h )
  
    r[i,0] = 0.5 * r[i-1,0] + sum * h

    #paso 5
    #uso de la ecuacion 4.35 (Extrapolacion de Richardson)
    powerOf4 = 1
    for j in range( 1, i + 1 ):
      powerOf4 = 4 * powerOf4
      #paso 6
      r[i,j] = r[i,j-1] + ( r[i,j-1] - r[i-1,j-1] ) / ( powerOf4 - 1 )
  #paso9
  return r
