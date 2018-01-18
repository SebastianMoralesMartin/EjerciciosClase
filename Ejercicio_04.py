# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_04

segundos = int(input("Teclea los segundos que han pasado: "))

h = segundos // 3600
m = (segundos % 3600) // 60
s = (segundos % 3600) % 60

print("La hora es %02i:%02i:%02i exactamente." % (h, m, s))
