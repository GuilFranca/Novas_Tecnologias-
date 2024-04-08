def verificar_primo(numero):
    # Se o número for menor ou igual a 1, não é primo
    if numero <= 1:
        return False

    # Inicializa uma lista de booleanos indicando se cada número é primo
    # Inicialmente, consideramos que todos os números são primos
    primos = [True] * (numero + 1)
    primos[0] = primos[1] = False  # 0 e 1 não são primos

    # Executa o Crivo de Eratóstenes
    for i in range(2, int(numero ** 0.5) + 1):
        if primos[i]:
            # Marca todos os múltiplos de i como não primos
            for j in range(i * i, numero + 1, i):
                primos[j] = False

    return primos[numero]


def main():
    # Solicita ao usuário que insira um número
    numero = int(input("Digite um número inteiro positivo: "))

    # Verifica se o número é primo
    if verificar_primo(numero):
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")


if __name__ == "__main__":
    main()
