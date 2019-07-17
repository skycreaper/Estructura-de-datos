"""
@author: Juan Camilo Sarmiento
version: 3.7.4
"""
print(" *** Diseñar un script quesolicite al usuario 5 nombres y losguarde en una tupla, una lista, y un conjunto.*** \n")

tupla = ()
lista = []
conjunto = set()

for i in range(5):
    nombre = input("{}. Ingrese un nombre: ".format(i+1))
    tupla += (nombre,)
    lista.append(nombre)
    conjunto.add(nombre)

print("Tupla: {}".format(tupla))
print("Lista: {}".format(lista))
print("Conjunto: {}".format(conjunto))