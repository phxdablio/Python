import csv

def mostrar_menu():
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("4 - Sair")

def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    agenda.append({"Nome": nome, "Telefone": telefone, "Email": email})
    print("Contato adicionado com sucesso!")

def buscar_contato(agenda):
    nome = input("Digite o nome do contato que deseja buscar: ")
    encontrados = []
    for contato in agenda:
        if contato["Nome"] == nome:
            encontrados.append(contato)
    if encontrados:
        print("Contatos encontrados:")
        for contato in encontrados:
            print("Nome:", contato["Nome"])
            print("Telefone:", contato["Telefone"])
            print("Email:", contato["Email"])
    else:
        print("Contato não encontrado.")

def listar_contatos(agenda):
    for contato in agenda:
        print("Nome:", contato["Nome"])
        print("Telefone:", contato["Telefone"])
        print("Email:", contato["Email"])

def salvar_agenda(agenda):
    with open('agenda.csv', 'w', newline='') as arquivo:
        cabecalho = ["Nome", "Telefone", "Email"]
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
        escritor.writeheader()
        for contato in agenda:
            escritor.writerow(contato)
    print("Agenda salva com sucesso!")

def carregar_agenda():
    agenda = []
    try:
        with open('agenda.csv', 'r', newline='') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                agenda.append(linha)
    except FileNotFoundError:
        print("Arquivo da agenda não encontrado. Criando uma nova agenda...")
    return agenda

def main():
    agenda = carregar_agenda()
    while True:
        mostrar_menu()
        opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            adicionar_contato(agenda)
        elif opcao == '2':
            buscar_contato(agenda)
        elif opcao == '3':
            listar_contatos(agenda)
        elif opcao == '4':
            salvar_agenda(agenda)
            break
        else:
            print("Opção inválida. Por favor, digite uma opção válida.")

if __name__ == "__main__":
    main()
