def separar_digitos(numero):
    numero_str = str(numero)
    for digito in numero_str:
        print(digito, end="   ")

numero = int(input("Digite um número de cinco dígitos: "))

if len(str(numero)) != 5:
    print("Por favor, digite um número de cinco dígitos.")
else:
    print("Os dígitos separados por três espaços são:")
    separar_digitos(numero)
