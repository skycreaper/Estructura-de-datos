#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: David Santos
version: 3.7.3
"""
print(" *** Ingresar un numero y calcular la suma desde el 1 hasta el numero ingresado *** \n")
num = int(input("Ingrese un numero para calcular: "))
r = 0
for x in range(1, num + 1):
    r += x
    print("la suma desde 1 hasta el numero ingresado %d es: %d" %(num, r))
