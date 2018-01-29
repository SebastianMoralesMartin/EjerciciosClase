# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_07

def calcularDiasVividos(a, m):
    da = a*365
    dm = m*30
    dab = a//4
    return da + dm + dab
def main():
    edadA = int(input("Teclea tu edad en años enteros: "))
    mesesA = int(input("Teclea los meses que han pasado desde tu cumpleaños: "))
    dias = calcularDiasVividos(edadA, mesesA)
    print("Has vivido %d días aprox." % dias)


main()
