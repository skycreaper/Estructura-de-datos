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
print("EJERCICIOS NUMPY CUARTO PUNTO")
#cree una matriz 6x6 cuya diagonal sea [1,2,3,4,5,6] e imprima una matriz
diagonal = np.diagflat([[1, 2], [3, 4], [5, 6]])
print("matriz 6x6: \n {}".format(diagonal) )
