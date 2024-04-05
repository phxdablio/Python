def calcular_digito_verificador(numero_conta):
    soma_digitos = sum(int(d) for d in str(numero_conta))
    digito_verificador = soma_digitos % 10
    return digito_verificador

numero_conta = input("Digite o número da conta (até seis dígitos): ")
digito_verificador = calcular_digito_verificador(numero_conta)
print(f"Número de conta completo: {numero_conta}-{digito_verificador}")
