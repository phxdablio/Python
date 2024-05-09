frase = input("Digite uma frase: ")

contagem_caracteres = {}
for char in frase:
    if char in contagem_caracteres:
        contagem_caracteres[char] += 1
    else:
        contagem_caracteres[char] = 1

print(contagem_caracteres)
