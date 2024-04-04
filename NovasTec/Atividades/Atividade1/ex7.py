total_segundos = int(input("Digite a quantidade de segundos: "))

dias = total_segundos // (24 * 3600)
resto = total_segundos % (24 * 3600)
horas = resto // 3600
resto %= 3600
minutos = resto // 60
segundos = resto % 60

print("Dias:", dias)
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)
