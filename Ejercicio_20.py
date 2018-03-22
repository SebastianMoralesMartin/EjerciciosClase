# Sebastian Morales Martin
# encoding: UTF-8
# Ejercicio_20: listas (pendejas)

def invertir(lista):
    contador = len(lista) - 1
    nuevaLista = []
    for numero in lista:
        nuevaLista.append(lista[contador])
        contador -= 1
    return nuevaLista



def main():
    listaValores = []
    valor = int(input('Valor a agregar (Teclea "-1" para terminar la lista): '))
    while valor != -1:
        listaValores.append(valor)
        valor = int(input('Valor a agregar (Teclea "-1" para terminar la lista): '))
    print("Datos: ", listaValores)
    print("Número de datos: ", len(listaValores))
    if len(listaValores)>0:
        print("Dato mayor: ", max(listaValores))
        print("Dato menor: ", min(listaValores))
        promedio = sum(listaValores)/ len(listaValores)
        print("Promedio: ", promedio)

    invertida = invertir(listaValores)
    print("Lista invertida: ", invertida)

main()