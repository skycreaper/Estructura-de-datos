#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: David Santos
version: 3.7.3
"""
print(" *** Preguntar si desea continuar hasta que se ingrese el caso negativo *** ")
while True:
    rta = input("Desea continuar s/n ? ")
    if rta == 'n' or rta == 'N' or rta == 'no' or rta == 'NO' or rta == 'No':
        break