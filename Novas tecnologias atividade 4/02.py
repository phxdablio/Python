lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]


print("Valores comuns às duas listas:", set(lista1) & set(lista2))
print("Valores que só existem na primeira lista:", set(lista1) - set(lista2))
print("Valores que existem apenas na segunda lista:", set(lista2) - set(lista1))
print("Elementos não repetidos das duas listas:", list(set(lista1) | set(lista2)))
print("Primeira lista sem os elementos repetidos na segunda:", list(set(lista1) - set(lista2)))
