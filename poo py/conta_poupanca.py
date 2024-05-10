from conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, aniversario_conta):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.aniversario_conta = aniversario_conta

    def calcular_juros_mensal(self, taxa_juros):
        juros = self.saldo * taxa_juros / 100
        self.saldo += juros
        self.historico.transacoes.append(f"Juros mensais de R$ {juros:.2f}")
