n = int(input("Numero de listas"))

listas = []
for _ in range(n):
    lista = set(input().split())
    listas.append(lista)


todas_as_palavras = [palavra for lista in listas for palavra in lista]
elementos_unicos = [palavra for palavra in todas_as_palavras if todas_as_palavras.count(palavra) == 1]

contagem = {}
for palavra in todas_as_palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

elementos_ultima_lista = listas[-1]
elementos_primeira_lista = listas[0]
diferenca = elementos_ultima_lista - elementos_primeira_lista

with open('listasSaida.txt', 'w') as f:
    f.write("Repetições: {")
    for chave, valor in contagem.items():
        f.write(f"'{chave}': {valor}, ")
    f.write("}\n")

    f.write(f"Elementos presentes na última lista mas não na primeira: {tuple(diferenca)}\n")
    f.write("Elementos que aparecem uma única vez: ")
    f.write(", ".join(elementos_unicos))
    f.write("\n")
