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
print("EJERCICIOS NUMPY SEGUNDO PUNTO")
#Escriba un programa para crear un arreglo de dimensión 10x4 y extraiga las primeras 3 filas de ese arreglo y guardelas en una variable llamada slice
matriz = np.empty((10, 4))
print("matriz 10x4: \n {}".format(matriz) )
sliceVar = matriz[0:3:]  #debido a que slice es una palabra reservada de python lo llamo sliceVar
print("slice: \n {}".format(sliceVar) )