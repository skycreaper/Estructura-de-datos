#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: David Santos
version: 3.7.3
"""
vocales = ("a", "e", "i", "o", "u")
while True:
    print(" *** Dado un caracter determinar si es una vocal *** \n")
    c = input("ingrese un caracter: ")
    if c in vocales:
        print("\n el caracter ingresado %s es una vocal" %c)
    else:
        print("\n Digite de nuevo otro caracter \n")