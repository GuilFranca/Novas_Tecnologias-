numero = input("Digite um número de cinco dígitos: ")

if len(numero) == 5 and numero.isdigit():
    digitos = [int(digito) for digito in numero]
    print(*digitos, sep="   ")
else:
    print("Por favor, insira um número válido de cinco dígitos.")
