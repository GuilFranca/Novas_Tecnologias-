# Lista de pedidos de sanduíches
sandwich_orders = ["Frango", "Carne", "Vegetariano", "Atum"]

# Lista de sanduíches prontos
finished_sandwiches = []

# Preparando cada sanduíche da lista de pedidos
for sandwich in sandwich_orders:
    print("Preparei seu sanduíche de", sandwich)
    finished_sandwiches.append(sandwich)

# Mostrando os sanduíches preparados
print("\nSanduíches preparados:")
for sandwich in finished_sandwiches:
    print(sandwich)
