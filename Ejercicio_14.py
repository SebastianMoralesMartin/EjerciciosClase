# encoding: UTF-8
# Sebastian Morales Martin
# Ejercico_14: Tablas de multiplicar con ciclos for

def imprimirTabla(valor):
    print('\nTabla del %d: \n'% valor)
    for factor in range(1, 11):
        total = valor * factor
        print('%d x %02d = %2.2f' %(valor, factor, total))

def main():
    for numero in range (1, 11):
        imprimirTabla(numero)

main()