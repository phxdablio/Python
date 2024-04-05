def adicao(num):
    for i in range(1, 11):
        print(f"{num} + {i} = {num + i}")

def subtracao(num):
    for i in range(1, 11):
        print(f"{num} - {i} = {num - i}")

def multiplicacao(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

def divisao(num):
    for i in range(1, 11):
        if i != 0:
            print(f"{num} / {i} = {num / i}")

while True:
    print("Menu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 1:
        num = int(input("Digite um número para a adição: "))
        adicao(num)
    elif escolha == 2:
        num = int(input("Digite um número para a subtração: "))
        subtracao(num)
    elif escolha == 3:
        num = int(input("Digite um número para a multiplicação: "))
        multiplicacao(num)
    elif escolha == 4:
        num = int(input("Digite um número para a divisão: "))
        divisao(num)
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
