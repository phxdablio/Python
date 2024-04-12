lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
print (f"O maior numero da lista{max(lista)}")
print (f"O menor numero da lista {min(lista)}")

pares = []
for n_pares in lista:
    if n_pares % 2 ==0:
        pares.append(n_pares)
print (f"Numeros pares da lista são: {pares}")

soma = sum(lista)
media = soma/len(lista)

print (f"A media da lista eh {media}")

lista_negativa = []
for negativo in lista:
    if negativo <= 0:
        lista_negativa.append(negativo)
        

soma_negativa = sum(lista_negativa)
print (f"A soma dos numeros negativos sao {soma_negativa}")

