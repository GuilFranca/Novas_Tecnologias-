def verificar_primo(numero):
    # Verifica se o número é menor ou igual a 1
    if numero <= 1:
        return False
    # Verifica se o número é divisível por algum número além de 1 e ele mesmo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

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
