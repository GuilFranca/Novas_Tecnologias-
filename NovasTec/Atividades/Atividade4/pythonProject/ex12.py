# Criando dicionários para representar animais de estimação
pet1 = {
    "nome": "Max",
    "tipo": "Cachorro",
    "dono": "João"
}

pet2 = {
    "nome": "Whiskers",
    "tipo": "Gato",
    "dono": "Maria"
}

pet3 = {
    "nome": "Nibbles",
    "tipo": "Coelho",
    "dono": "Carlos"
}

# Armazenando os dicionários em uma lista chamada pets
pets = [pet1, pet2, pet3]

# Percorrendo a lista de animais de estimação e apresentando as informações sobre cada um
for pet in pets:
    print("Nome:", pet["nome"])
    print("Tipo:", pet["tipo"])
    print("Dono:", pet["dono"])
    print()  # Adiciona uma linha em branco para separar as informações de cada animal de estimação
