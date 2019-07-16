"""
@author: David Santos
"""
complejos = [1 + 3j, 2 - 5j, 4 + 2j, 5 - 5j, 20 + 3j, 3.1415 + 2j]
print("la lista de complejos es: {} \n".format(complejos) )
magnitud = [abs(x) for x in complejos]
print ("la magnitud de la lista de complejos es {}".format(magnitud) )