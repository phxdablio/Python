versao_inicial = [1, 2, 3, 4, 5]
versao_alterada = [2, 3, 4, 6, 7]


print("Elementos que não mudaram:", set(versao_inicial) & set(versao_alterada))
print("Novos elementos:", set(versao_alterada) - set(versao_inicial))
print("Elementos removidos:", set(versao_inicial) - set(versao_alterada))
