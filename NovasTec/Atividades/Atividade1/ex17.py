def calcular_digito_verificador(numero_conta):
    # Calcula a soma dos dígitos do número da conta
    soma_digitos = sum(int(digito) for digito in str(numero_conta))

    # Calcula o dígito verificador
    digito_verificador = soma_digitos % 10

    # Retorna o número de conta completo
    return f"00{numero_conta}-{digito_verificador}"

def main():
    # Solicita ao usuário inserir o número da conta
    numero_conta = input("Digite o número da conta (até seis dígitos): ")

    # Verifica se o número da conta tem até seis dígitos
    if len(numero_conta) > 6:
        print("O número da conta deve ter até seis dígitos.")
        return

    # Calcula e imprime o número de conta completo
    numero_completo = calcular_digito_verificador(numero_conta)
    print("Número de conta completo:", numero_completo)

if __name__ == "__main__":
    main()
