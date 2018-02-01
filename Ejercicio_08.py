# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_08

def calcularIF(cantidad):
    impuesto = cantidad * 0.16
    return impuesto

def calcularIE(cantidad):
    impuesto = cantidad * 0.03
    return impuesto

def total(cantidad, impuesto):
    return cantidad + impuesto

def impuestoTotal(impuesto1, impuesto2):
    return impuesto1 + impuesto2

def main():
    subT = float(input('Subtotal de compra: '))
    impFed = calcularIF(subT)
    impEst = calcularIE(subT)
    impT = impuestoTotal(impEst, impFed)
    tot = total(subT, impT)
    print('---------------------------------------------------------------------\n-Subtotal: %10.2f\n-Impuesto Federal: %10.2f\n-Impuesto Estatal: %10.2f\n-Total Impuestos: %10.2f\n-TOTAL: %10.2f\n---------------------------------------------------------------------' % (subT, impFed, impEst, impT, tot))

main()