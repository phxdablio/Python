pets = [
    {"animal": "cachorro", "tipo": "mamífero", "dono": "João"},
    {"animal": "gato", "tipo": "mamífero", "dono": "Maria"},
    {"animal": "pássaro", "tipo": "ave", "dono": "Pedro"}
]

for pet in pets:
    print("\nInformações sobre o animal de estimação:")
    for chave, valor in pet.items():
        print(f"{chave}: {valor}")
