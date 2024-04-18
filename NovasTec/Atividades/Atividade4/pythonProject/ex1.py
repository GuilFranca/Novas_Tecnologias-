def contar_caracteres(frase):
    # Inicializa um dicionário vazio para armazenar a contagem de caracteres
    contagem = {}

    # Itera sobre cada caractere na frase
    for caractere in frase:
        # Verifica se o caractere já está no dicionário
        if caractere in contagem:
            # Se estiver, incrementa o valor correspondente à chave
            contagem[caractere] += 1
        else:
            # Se não estiver, adiciona a chave ao dicionário com o valor inicial de 1
            contagem[caractere] = 1

    return contagem


# Função para entrada do usuário e chamada da função contar_caracteres
def main():
    frase = input("Digite uma frase: ")
    # Converte a frase para minúsculas para evitar diferenciação entre maiúsculas e minúsculas
    frase = frase.lower()
    resultado = contar_caracteres(frase)
    print(resultado)


if __name__ == "__main__":
    main()
