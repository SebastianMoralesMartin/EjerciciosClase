# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_15



def main():
    numeroAprobadas = 0
    sumaAprobadas = 0
    for k in range(1, 6):
        calificacion = int(input('Calificación %s: '% k))
        if calificacion>=70:
            numeroAprobadas = numeroAprobadas + 1
            sumaAprobadas += calificacion

    #promediar
    if numeroAprobadas>0:
        promedio = sumaAprobadas / numeroAprobadas
        print('Promedio %.2f'% promedio)
    else: print('No hay promedio')

main()
