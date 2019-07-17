"""
@author: Juan Camilo Sarmiento
version: 3.7.4
"""
print(" *** Escribir un programa que dado un diccionario de 5 nombres cuyas claves son los números del 1\n"+
" establezca cuál es el nombre de mayor longitud y diga cuál es su clave.*** \n")

nombres = {}
for x in range(5):
    nombres[x+1] = input("Escribe un nombre: ")

clave = 1
mayor = nombres[clave]

for i in nombres:
    if len(nombres[i]) > len(mayor):
        mayor = nombres[i]
        clave = i

print("\nEl nombre de mayor longitud es {} y su clave es {}".format(mayor, clave))