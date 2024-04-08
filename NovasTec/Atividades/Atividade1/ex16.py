def fibonacci(n):
    if n <= 0:
        return "A série de Fibonacci começa a partir do índice 1."
    elif n == 1 or n == 2:
        return 1
    else:
        fib_antes = 1
        fib_atual = 1
        for _ in range(3, n + 1):
            fib_prox = fib_antes + fib_atual
            fib_antes = fib_atual
            fib_atual = fib_prox
        return fib_atual


def main():
    # Solicita ao usuário inserir um número
    n = int(input("Digite o índice da série de Fibonacci que você deseja calcular: "))

    # Calcula e imprime o n-ésimo termo da série de Fibonacci
    termo = fibonacci(n)
    print(f"O {n}-ésimo termo da série de Fibonacci é: {termo}")


if __name__ == "__main__":
    main()
