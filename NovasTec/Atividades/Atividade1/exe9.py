while True:
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == '1':
        print("Tabuada de Adição:")
        for i in range(1, 11):
            for j in range(1, 11):
                print(f"{i} + {j} = {i + j}")
    elif opcao == '2':
        print("Tabuada de Subtração:")
        for i in range(1, 11):
            for j in range(1, 11):
                print(f"{i} - {j} = {i - j}")
    elif opcao == '3':
        print("Tabuada de Multiplicação:")
        for i in range(1, 11):
            for j in range(1, 11):
                print(f"{i} * {j} = {i * j}")
    elif opcao == '4':
        print("Tabuada de Divisão:")
        for i in range(1, 11):
            for j in range(1, 11):
                if j != 0:
                    print(f"{i} / {j} = {i / j}")
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
