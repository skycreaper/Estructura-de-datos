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
print("EJERCICIOS NUMPY QUINTO PUNTO")
m5x3 = np.random.rand(5, 3)
m3x2 = np.random.rand(3, 2)
print("matriz 5x3: \n {}".format(m5x3) )
print("matriz 3x2: \n {}".format(m3x2) )
dot = np.dot(m5x3,m3x2)
print("dot: \n {}".format(dot) )