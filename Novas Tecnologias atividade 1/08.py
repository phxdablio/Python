def converter_segundos(segundos):
    dias = segundos // (24 * 3600)
    segundos %= (24 * 3600)
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return dias, horas, minutos, segundos

segundos = int(input("Digite a quantidade de segundos: "))
dias, horas, minutos, segundos_restantes = converter_segundos(segundos)
print(f"{dias} dias, {horas} horas, {minutos} minutos, {segundos_restantes} segundos")
