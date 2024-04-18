def comparar_versoes(versao_inicial, versao_modificada):
    # Converte as listas em conjuntos para facilitar a manipulação
    set_versao_inicial = set(versao_inicial)
    set_versao_modificada = set(versao_modificada)

    # Elementos que não mudaram
    nao_mudaram = set_versao_inicial.intersection(set_versao_modificada)
    print("Elementos que não mudaram:", nao_mudaram)

    # Novos elementos
    novos_elementos = set_versao_modificada.difference(set_versao_inicial)
    print("Novos elementos:", novos_elementos)

    # Elementos que foram removidos
    removidos = set_versao_inicial.difference(set_versao_modificada)
    print("Elementos removidos:", removidos)


# Exemplo de utilização
versao_inicial = [1, 2, 3, 4, 5]
versao_modificada = [4, 5, 6, 7, 8]

comparar_versoes(versao_inicial, versao_modificada)
