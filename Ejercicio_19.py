# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_19: Puntos extras
'''
def calcularRaiz(a):
    x = a/2
    while ((x*x -a)**2)**0.5 >.00001:
        print(x)
        x = (x + a/x)/2
    return x


def main():
    a = int(input('a: '))
    raiz = calcularRaiz(a)
    print('La raiz cuadrada de %d es %f'%(a, raiz))

#main()

def forConWhile():
    contador = 0
    while contador < 100:
        print(contador)
        contador += 1

forConWhile()
'''

def invertirNumeros(valor):
    acumulador = 0
    while valor != 0:
        unidad = valor %10
        valor = valor //10
        acumulador = acumulador * 10 + unidad

    return acumulador


def main():
    valor = int(input('Teclea el Valor a invertir: '))
    print(invertirNumeros(valor))

main()