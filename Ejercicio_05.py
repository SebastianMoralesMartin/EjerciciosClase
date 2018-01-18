# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_05

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

raiz1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
raiz2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print("raíz 1: %.2f" % raiz1)
print("raíz 2: %.2f" % raiz2)
