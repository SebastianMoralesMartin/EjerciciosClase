# encoding: UTF-8
# Sebastian Morales Martín
# Ejercicio_23

def sumarListas(lista1, lista2):
    nLista = []
    if len(lista1) > len(lista2):
        indice = lista1
    elif len(lista2) > len(lista1):
        indice = lista2
    elif len(lista1) == len(lista2):
        indice = lista1
    for numero in range(len(indice)):
        subindice = lista1[numero] + lista2[numero]
        nLista.append(subindice)
    return nLista

lista1 = [1,2,3,4,5]
lista2 = [5,4,3,2,1]
print(sumarListas(lista1, lista2))