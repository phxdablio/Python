from datetime import datetime

class Historico:
    def __init__(self):
        self.data_da_abertura = datetime.now()
        self.transacoes = []

    def imprime(self):
        for transacao in self.transacoes:
            print(transacao)

class ContaBancaria:
    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def consultar_saldo(self):
        return self.saldo

    def saca(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.historico.transacoes.append(f"Saque de R$ {valor:.2f}")
            return True
        else:
            return False

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Depósito de R$ {valor:.2f}")

    def transfere_para(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            self.historico.transacoes.append(f"Transferência de R$ {valor:.2f} para {destino.numero_agencia} - {destino.tipo_conta}")
            destino.historico.transacoes.append(f"Transferência recebida de R$ {valor:.2f} de {self.numero_agencia} - {self.tipo_conta}")
            return True
        else:
            return False

    def obter_extrato(self):
        self.historico.imprime()

    def alterar_titular(self, novo_titular):
        self.titular = novo_titular

    def fechar_conta(self):
        self.titular = None
