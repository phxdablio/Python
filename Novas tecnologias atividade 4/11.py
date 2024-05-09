pessoa1 = {
    "first_name": "João",
    "last_name": "Silva",
    "age": 30,
    "city": "São Paulo"
}

pessoa2 = {
    "first_name": "Maria",
    "last_name": "Santos",
    "age": 25,
    "city": "Rio de Janeiro"
}

people = [pessoa1, pessoa2]

for pessoa in people:
    print("\nInformações sobre a pessoa:")
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")
