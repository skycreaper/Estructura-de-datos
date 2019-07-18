#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: David Santos
version: 3.7.3
"""
print(" *** Mostrar la suma de los cuadrados del 1 a 100 *** \n")
r = 0
for x in range(1, 101):
    r += x ** 2
print("la suma de los cuadrados es: %d" %r)