def encontrar_primos(n):
    primos = []
    numero = 2

    while len(primos) < n:
        if verificar_primo(numero):
            primos.append(numero)
        numero += 1

    return primos


def main():
    # Solicita ao usuário que insira um número
    n = int(input("Digite a quantidade de números primos que você deseja encontrar: "))

    # Encontra os n primeiros números primos
    primeiros_primos = encontrar_primos(n)

    # Imprime os n primeiros números primos
    print(f"Os {n} primeiros números primos são:", primeiros_primos)


def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
