#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: David Santos
version: 3.7.3
"""
dias = [(1, "lunes"), (2, "martes"), (3, "miercoles"), (4, "jueves"), (5, "viernes"), (6, "sabado"), (7, "domingo")]
def dias_de_la_semana():
    while True:
        print(" *** Dado un numero ingresado si esta en el rango de 1 a 7 decir el dia correspondiente *** \n")
        x = int(input("Ingrese un numero: "))    
        if x > 0 and x < 8:
            print(dias[x - 1])
        else:
            print("por favor ingresa un numero entre 1 - 7 \n")
            pass

if __name__ == "__main__":
    dias_de_la_semana()