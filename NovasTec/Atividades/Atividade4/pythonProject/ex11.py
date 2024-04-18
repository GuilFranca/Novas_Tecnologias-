# Dicionário representando informações sobre uma pessoa
pessoa1 = {
    "first_name": "João",
    "last_name": "Silva",
    "age": 30,
    "city": "São Paulo"
}

# Outros dicionários representando informações sobre diferentes pessoas
pessoa2 = {
    "first_name": "Maria",
    "last_name": "Santos",
    "age": 25,
    "city": "Rio de Janeiro"
}

pessoa3 = {
    "first_name": "Carlos",
    "last_name": "Ferreira",
    "age": 35,
    "city": "Belo Horizonte"
}

# Lista contendo os dicionários de pessoas
people = [pessoa1, pessoa2, pessoa3]

# Percorrendo a lista de pessoas e apresentando as informações de cada pessoa
for pessoa in people:
    print("Nome:", pessoa["first_name"], pessoa["last_name"])
    print("Idade:", pessoa["age"])
    print("Cidade:", pessoa["city"])
    print()  # Adiciona uma linha em branco para separar as informações de cada pessoa
