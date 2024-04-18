def comparar_listas(lista1, lista2):
    # Converte as listas em conjuntos para facilitar a manipulação
    set1 = set(lista1)
    set2 = set(lista2)

    # a. os valores comuns às duas listas
    comuns = set1.intersection(set2)
    print("Valores comuns às duas listas:", comuns)

    # b. os valores que só existem na primeira lista
    apenas_na_primeira = set1.difference(set2)
    print("Valores que só existem na primeira lista:", apenas_na_primeira)

    # c. os valores que existem apenas na segunda lista
    apenas_na_segunda = set2.difference(set1)
    print("Valores que só existem na segunda lista:", apenas_na_segunda)

    # d. uma lista com os elementos não repetidos das duas listas
    elementos_unicos = set1.union(set2)
    print("Elementos não repetidos das duas listas:", elementos_unicos)

    # e. a primeira lista sem os elementos repetidos na segunda
    sem_repetidos_segunda = set1.difference(set2)
    print("Primeira lista sem os elementos repetidos na segunda:", sem_repetidos_segunda)


# Exemplo de utilização
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comparar_listas(lista1, lista2)
