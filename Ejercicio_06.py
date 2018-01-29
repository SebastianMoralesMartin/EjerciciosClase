# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_06: Funciones

def convertirFaC(gradosF):
    c = (gradosF-32)/1.8
    return c

def main():
    gradosF = int(input("Fahrenheit: "))
    gradosC = convertirFaC(gradosF)
    print("%i grados Fahrenheit son %.2f grados Celsius." % (gradosF, gradosC))

main()