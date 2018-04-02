#encoding: UTF-8
# Sebastian Morales Martín
# Ejercicio_21: palíndromos


def quitarEspacios(args):
    sinEspacios = []
    for numero in args:
        if numero != ' ':
            sinEspacios.append(numero)
    return sinEspacios


def invertirLista(lista):
    contador = len(lista) - 1
    nuevaLista = []
    for numero in lista:
        nuevaLista.append(lista[contador])
        contador -= 1
    return nuevaLista


def main():

    palindromo = input('Teclea el posible palindromo: ')
    cadena = palindromo.upper()
    listaOriginal = list(cadena)
    sinEspacios = quitarEspacios(listaOriginal)
    inversa = invertirLista(sinEspacios)
    if inversa == sinEspacios:
        print('%s es palindromo'% palindromo)
    else:
        print('%s no es palindromo' % palindromo)

main()