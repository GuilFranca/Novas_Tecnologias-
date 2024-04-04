import math

a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    # Calcula as raízes
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    # Imprime as raízes
    print(f"Raiz x': {raiz1}")
    print(f"Raiz x'': {raiz2}")
