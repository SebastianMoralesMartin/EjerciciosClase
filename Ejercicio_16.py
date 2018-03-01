# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_16: números primos y numeros perfectos

def esPerfecto(valor):
    ap= 0

    for k in range(1, valor):
        if valor%k == 0:
            ap += k
    if ap == valor:

        return True
    else:
        return False

def esPrimo(valor):
    cd = 0

    for numero in range(2, valor): # desde 2 hasta valor-1
        if valor % numero == 0:
            cd+= 1  #cd = cd + 1
    if cd == 0:
        return True
    else:
        return False



def main():
    for numero in range(1, 9999999999999999999999999999999):
        '''
        print('%02d es perfecto? %s\n'% (numero, esPerfecto(numero)))
        print(listaPerfectos)
        '''
        if esPerfecto(numero):
            print(numero)
main()