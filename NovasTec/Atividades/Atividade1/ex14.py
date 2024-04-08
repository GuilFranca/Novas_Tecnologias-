def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial


def main():
    # Solicita ao usuário inserir um número inteiro não negativo
    numero = int(input("Digite um número inteiro não negativo: "))

    # Calcula e imprime o fatorial do número
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")


if __name__ == "__main__":
    main()
