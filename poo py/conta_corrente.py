from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if self.cheque_especial:
            self.saldo -= valor
            self.historico.transacoes.append(f"Utilização do cheque especial de R$ {valor:.2f}")
            return True
        else:
            return False
