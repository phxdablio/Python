def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

numero = int(input("Digite um número não negativo para calcular o fatorial: "))
print(f"O fatorial de {numero} é {calcular_fatorial(numero)}.")
