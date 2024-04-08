def calcular_fatorial(n):
    if n < 0:
        return "O fatorial não está definido para números negativos."
    elif n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial


def main():
    # Solicita ao usuário inserir um número inteiro
    numero = int(input("Digite um número inteiro não negativo: "))

    # Calcula o fatorial do número
    resultado = calcular_fatorial(numero)

    # Imprime o resultado
    print(f"O fatorial de {numero} é: {resultado}")


if __name__ == "__main__":
    main()
