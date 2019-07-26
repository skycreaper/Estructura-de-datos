#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: David Steven Santos Santos
codigo: 20152020076
Ingenieria de sistemas
version: 3.7.3
"""
import numpy as np
print("*****************************************************************************************************************************")
print("EJERCICIOS NUMPY PRIMER PUNTO")
matrizPrueba = np.array([ [34,23,546,788],[12,1099,434,214],[1234,5454,6466,2323],[2332,657,896,53] ])
print("matriz: \n {}".format(matrizPrueba) )
#¿Cuál es el índice para el elemento 5454?
print("indice del elemento: \n {}".format(matrizPrueba[2,1]) )
#"Rebane" la matriz matrizPrueba de forma que seleccione las filas pares y todas sus columnas
print("filas pares y todas sus columnas: \n {}".format(matrizPrueba[0::2]) ) #start:stop:step considerando que se cuenta desde 0
matrizA = np.arange(12)
matrizB = np.arange(12)
print("matriz B: \n {}".format(matrizB) )
#Sacar la raíz cuadrada de los valores de la matriz B
print("Raiz cuadrada de la matrizB: \n {}".format(np.sqrt(matrizB).reshape((3,4))) )
#Cree una matriz de 4x4 y haga su transpuesta
matriz4b4 = np.empty((4, 4))
print("Matriz de 4x4: \n {}".format(matriz4b4))
print("Matriz transpuesta: \n {}".format(np.transpose(matriz4b4)) )
