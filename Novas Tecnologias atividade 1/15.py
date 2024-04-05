def calcular_quadrado(n):
    resultado = 0
    for i in range(1, n * 2, 2):
        resultado += i
    return resultado

numero = int(input("Digite um número para calcular seu quadrado: "))
print(f"O quadrado de {numero} é {calcular_quadrado(numero)}.")
