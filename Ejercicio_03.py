# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_03
peso = float(input("Introduce tu peso: "))
altura = float(input("Introduce tu altura en metros (Por ejemplo: 1.75): "))

imc = peso/altura**2

print("Tu IMC es de %10.2f" % imc)

if imc < 18.5:
    print("Sufres de bajo peso!!!")
elif imc >= 18.5 and imc < 25:
    print("Estas en tu peso ideal!!!")
elif imc >= 25 and imc < 27:
    print('Sufres de "Sobrepeso Tipo I"')
elif imc >= 27 and imc < 30:
    print('Sufres de "Sobrepeso Tipo II"')
elif imc >= 30 and imc < 35:
    print('Sufres de "Obesidad Tipo I"')
elif imc >= 35 and imc < 40:
    print('Sufres de "Obesidad Tipo II"')
elif imc >= 40 and imc < 50:
    print('Sufres de "Obesidad Tipo III (Mórbida)')
elif imc >= 50:
    print('Sufres de "Obesidad Tipo IV (Extrema)')
else:
    print("¿Cómo putas estas vivo?")
