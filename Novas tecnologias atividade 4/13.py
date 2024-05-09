sandwich_orders = ['atum', 'frango', 'queijo']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"Preparei seu sanduíche de {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\nSanduíches prontos:")
for sandwich in finished_sandwiches:
    print(sandwich)
