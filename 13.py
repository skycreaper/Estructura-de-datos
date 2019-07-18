#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: David Santos
version: 3.7.3
"""
print(" *** imprimir los numeros multiplos de 5 del 1 al 100 usando conjuntos por comprehension *** \n")
x = {i for i in range(1, 101) if i % 5 == 0} 
print(sorted(x) )