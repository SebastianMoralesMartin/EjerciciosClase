# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_13

def calcularEstado(valor):
    estado = ''
    if valor >= 100:
        estado= 'Vapor'
    elif valor >= 50:
        estado = 'Muy Caliente'
    elif valor >= 30:
        estado = 'Caliente'
    elif valor > 20:
        estado = 'Tibia'
    elif valor >= 10:
        estado = 'Fria'
    else:
        estado = 'Congelada'
    return estado


def main():
    temperatura = float(input('Teclea la Temperatura del awa: '))
    estado = calcularEstado(temperatura)
    print(estado)

main()