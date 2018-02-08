# encoding: UTF-8
# Sebastian Morales Martin
#Ejercicio_10

def resolverDiferencia(a, b):
    if a<b:
        return b
    elif a>b:
        return a
    else:
        mensaje = ("%d son los mismos, ninguno es mayor" % a)
        return mensaje

def main():
    numero1 = int(input("Teclea el primer número: "))
    numero2 = int(input("Teclea el segundo número: "))
    numeroGanador= resolverDiferencia(numero1, numero2)

    print(numeroGanador)


main()
