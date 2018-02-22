# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_12

def calcularDia(dia, mes, anio):
    y0 = anio - (14-mes)//12
    x = y0 + y0//4 - y0//100 + y0//400
    m0 = mes + (12*((14-mes)//12)) - 2
    d0 = (dia + x + (31*m0//12)) % 7
    return d0
def calcularNombre(valor):
        if valor == 0:
            return "Domingo"
        elif valor == 1:
            return "Lunes"
        elif valor == 2:
            return "Martes"
        elif valor == 3:
            return "Miercoles"
        elif valor == 4:
            return "Jueves"
        elif valor == 5:
            return "Viernes"
        elif valor == 6:
            return "Sabado"
        else:
            return 'Ese dia no existe prro :v'

def main():
    dia= int(input('Día: '))
    mes =  int(input('\nMes: '))
    anio = int(input('\nAño: '))
    d0 = calcularDia(dia, mes, anio)
    diaSemana = calcularNombre(d0)
    print("El día es: %s" % diaSemana)

main()
