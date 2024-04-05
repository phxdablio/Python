def separar_digitos(numero):
    numero_str = str(numero)
    for digito in numero_str:
        print(digito, end="   ")

numero = int(input("Digite um número: "))

print("Os dígitos separados por três espaços são:")
separar_digitos(numero)
