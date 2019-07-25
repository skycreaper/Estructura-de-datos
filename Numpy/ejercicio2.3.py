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
print("EJERCICIOS TERCER PUNTO")
#haga 2 arreglos unidimensionales con valores aleatorios y determinen si son iguales
vector1 = np.random.rand(15)
vector2 = np.random.rand(15)
print("Vector 1: \n {}".format(vector1) )
print("Vector 2: \n {}".format(vector2) )
print("son iguales: %s" %np.array_equal(vector1, vector2) )