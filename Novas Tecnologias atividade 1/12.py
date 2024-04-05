def imprimir_primos(n):
    count = 0
    numero = 2
    while count < n:
        if verificar_primo(numero):
            print(numero, end=" ")
            count += 1
        numero += 1

n = int(input("Digite um número para imprimir os primeiros números primos: "))
print(f"Os primeiros {n} números primos são:")
imprimir_primos(n)
