numero = input("Digite um número: ")

if numero.isdigit():
    digitos = [int(digito) for digito in numero]
    print(*digitos, sep="   ")
else:
    print("Por favor, insira apenas números.")
