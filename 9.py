#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Juan Camilo Sarmiento
version: 3.7.4
"""
print(" *** imprimir los numeros del 1 al 10 en tipo string y mostrar el tipo para verificar *** \n")
numeros = [str(i) for i in range(1,11)]
for x in numeros:
    print("{} :{}".format(x,type(x)))
