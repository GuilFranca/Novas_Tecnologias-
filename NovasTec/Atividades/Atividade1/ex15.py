def calcular_quadrado(n):
    if n <= 0:
        return "O quadrado está definido apenas para números naturais positivos."
    else:
        soma_impares = 0
        ultimo_impar = 1
        for _ in range(n):
            soma_impares += ultimo_impar
            ultimo_impar += 2
        return soma_impares


def main():
    # Solicita ao usuário inserir um número natural
    numero = int(input("Digite um número natural: "))

    # Calcula e imprime o quadrado usando a soma de ímpares
    resultado = calcular_quadrado(numero)
    print(f"O quadrado de {numero} é: {resultado}")


if __name__ == "__main__":
    main()
