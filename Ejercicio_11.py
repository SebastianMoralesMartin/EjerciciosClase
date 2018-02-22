# endcoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_11
'''
import getpass
def buscarDia(valor):
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
    usuario = getpass.getuser()
    print('Hola %s!!!\n' % usuario)

    numDia = int(input('Teclea el dia de la semana: '))
    dia = buscarDia(numDia)
    print('El dia es "%s"' % dia)


main()
'''