# modulo para iteracion punto fijo e iteracion Gauss-Seidel
#Autor: Alexis Tercero (@math.by.uri) 

import numpy as np
import matplotlib.pyplot as plt

def grafica(x,y):
  plt.plot(x,y)
  plt.show()

#implementacion de norma del supremo
def norma(x1,x0):
  '''x1,x2: list'''
  delta = np.abs(np.array(x1) - np.array(x0))
  return max(delta)

#------------------------------------------------------------------------------
# IMPLEMENTACION PARA G:R^2->R^2

#proceso de solucion del sistema
def IteracionPuntoFijo(X,g1,g2):
  ''' 
  Parametros:
  X: list. ej X0 = [x1,x2]
  g1: function (x1,x2) 
  g2: function (x1,x2)

  Retorna la solucion del sistema en caso de ser encontrada
  con una exactitud de 1e-5
  en caso contrario se imprime una bandera.
  '''
  #Proceso iterativo
  print('Iteracion punto fijo')
  print('punto inicial x0:',X)

  tol = 1e-5 #exacitud de 0.00001
  nmi = 30 #numero maximo de iteraciones

  #datos para grafica de dispersion
  x = []
  y = []

  i = 1
  while i < nmi:
    #calcula los componentes del punto fijo aproximado y los almacena para graficar
    x.append(g1(*X))
    y.append(g2(*X))

    #Se mide el error
    delta = norma( [x[-1], y[-1]] ,X)

    #Se actualiza el valor actual
    X = [ x[-1], y[-1]]

    #se presentan datos resultados por iteracion
    print('punto x{}:'.format(i),X , 'error: ', delta )

    #Se evalua la exactitud de nuestra solucion
    if delta < tol:
      print('\n\nLa solucion es: ({:.5f},{:.5f})'.format(X[0],X[1]))
      break

    i+=1#se prosigue con la iteracion
  else:
    print('No se llego a la solucion')
  
  grafica(x,y)
  return X
#-------------------------------------------------
def IteracionGaussSeidel(X,g1,g2):
  ''' Parametros: 
  X: list. ej X0 = [x1,x2]
  g1: function (x1,x2)
  g2: function (x1,x2)
  
  Retorna la solucion del sistema en caso de ser encontrada
  con una exactitud de 1e-5
  en caso contrario se imprime una bandera.
  '''
  #Proceso iterativo
  print('Iteracion Gauss Seidel')
  print('punto inicial x0:',X)

  tol = 1e-5 #exacitud de 0.00001
  nmi = 30 #numero maximo de iteraciones

  #datos para grafica de dispersion
  x = []
  y = []

  i = 1
  while i < nmi:
    #calcula los componentes del punto fijo aproximado y los almacena para graficar
    x.append(g1(*X))
    X = [x[-1],X[-1]] # variacion del metodo de Gauss-Seidel.
    y.append(g2(*X))

    #Se mide el error
    delta = norma( [x[-1], y[-1]] ,X)

    #Se actualiza el valor actual
    X = [ x[-1], y[-1]]

    #se presentan datos resultados por iteracion
    print('punto x{}:'.format(i),X , 'error: ', delta )

    #Se evalua la exactitud de nuestra solucion
    if delta < tol:
      print('\n\nLa solucion es: ({:.5f},{:.5f})'.format(X[0],X[1]))
      break

    i+=1#se prosigue con la iteracion
  else:
    print('No se llego a la solucion')
  
  grafica(x,y)
  return X

#------------------------------------------------------------------------------
# IMPLEMENTACION PARA G:R^3->R^3
#proceso de solucion del sistema
def IteracionPuntoFijo3D(X,g1,g2,g3):
  ''' 
  Parametros:
  X: []. ej X0 = [x1,x2,x3]
  g1: function (X) donde X: []
  g2: function (X)

  Retorna la solucion del sistema en caso de ser encontrada
  con una exactitud de 1e-5
  en caso contrario se imprime una bandera.
  '''
  #Proceso iterativo
  print('Iteracion Punto fijo')
  print('punto inicial x0:',X)

  tol = 1e-5 #exacitud de 0.00001
  nmi = 30 #numero maximo de iteraciones

  #datos para grafica de dispersion
  x = []
  y = []
  z = []

  i = 1
  while i < nmi:
    #calcula los componentes del punto fijo aproximado y los almacena para graficar
    x.append(g1(*X))
    y.append(g2(*X))
    z.append(g3(*X))

    #Se mide el error
    delta = norma( [x[-1], y[-1],z[-1]] ,X)

    #Se actualiza el valor actual
    X = [ x[-1], y[-1],z[-1]]

    #se presentan datos resultados por iteracion
    print('punto x{}:'.format(i),X , 'error: ', delta )

    #Se evalua la exactitud de nuestra solucion
    if delta < tol:
      print('\n\nLa solucion es: ({:.5f},{:.5f},{:.5f})'.format(X[0],X[1],X[2]))
      break

    i+=1#se prosigue con la iteracion
  else:
    print('No se llego a la solucion')
  
  #grafica(x,y,z)
  return X
#-------------------------------------------------
def IteracionGaussSeidel3d(X,g1,g2,g3):
  ''' 
  Parametros:
  X: []. ej X0 = [x1,x2,x3]
  g1: function (X) donde X: []
  g2: function (X)

  Retorna la solucion del sistema en caso de ser encontrada
  con una exactitud de 1e-5
  en caso contrario se imprime una bandera.
  '''
  #Proceso iterativo
  print('Iteracion Gauss Seidel')
  print('punto inicial x0:',X)

  tol = 1e-5 #exacitud de 0.00001
  nmi = 30 #numero maximo de iteraciones

  #datos para grafica de dispersion
  x = []
  y = []
  z = []

  i = 1
  while i < nmi:
    #calcula los componentes del punto fijo aproximado y los almacena para graficar
    x.append(g1(*X))
    X = [x[-1],X[1],X[2]] # variacion del metodo de Gauss-Seidel.
    y.append(g2(*X))
    X = [X[0],y[-1],X[2]] # variacion del metodo de Gauss-Seidel.
    z.append(g3(*X))

    #Se mide el error
    delta = norma( [x[-1], y[-1],z[-1]] ,X)

    #Se actualiza el valor actual
    X = [ x[-1], y[-1],z[-1]]

    #se presentan datos resultados por iteracion
    print('punto x{}:'.format(i),X , 'error: ', delta )

    #Se evalua la exactitud de nuestra solucion
    if delta < tol:
      print('\n\nLa solucion es: ({:.5f},{:.5f},{:.5f})'.format(X[0],X[1],X[2]))
      break

    i+=1#se prosigue con la iteracion
  else:
    print('No se llego a la solucion')
  
  #grafica(x,y,z)
  return X
  #------------------------------------------------------------------------------