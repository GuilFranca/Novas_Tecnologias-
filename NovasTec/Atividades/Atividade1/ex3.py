def ver_par_imp(num):
    if num % 2 == 0:
        return "par"
    else:
        return "ímpar"

try:
    num = int(input("Digite um número inteiro: "))
    result = ver_par_imp(num)
    print(f"O número {num} é {result}.")
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")