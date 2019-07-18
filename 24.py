#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Juan Camilo Sarmiento
version: 3.7.4
"""
print(" *** Escribir un programa que, dada una lista con números en notación científica"+
" genere un diccionario con clave el número en notación decimal y el valor del número en notación cientifica (como un string)"+
" finalmente, imprima aquellos números cuyo número en la clave sea menor que 0.01. *** \n")

numeros_cientificos = [-0.5e-3, 35.12e-2, 0.4E2, 0.1e-2, +1e-04]

diccionario = {float(""+str(x)):str(x) for x in numeros_cientificos}

print(diccionario)

for key in diccionario:
    if key < 0.01:
        print(diccionario[key])