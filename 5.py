"""
@author: David Santos
version: 3.7.3
"""
print(" *** Dada una lista de numeros complejos convertir la parte real como la clave y la parte imaginaria como el valor en un diccionario *** \n")
complejos = [1 + 3j, 2 - 5j, 4 + 2j, 5 - 5j, 20 + 3j, 3.1415 + 2j]
dic = {x.real: x.imag for x in complejos} # al imprimir solamente el numero imaginario este toma el valor de un flotante por eso la j no se muestra
print(dic)
