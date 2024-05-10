from conta_bancaria import ContaBancaria, Historico
from cliente import Cliente
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente


cliente1 = Cliente("João", "Silva", "123.456.789-00")
cliente2 = Cliente("Maria", "Santos", "987.654.321-00")

conta1 = ContaBancaria("001", "Corrente", 1000.0, 500.0)
conta2 = ContaBancaria("002", "Poupança", 500.0, 0.0)


conta_poupanca = ContaPoupanca("003", "Poupança", 1000.0, 0.0, "01/01/2024")

conta_corrente = ContaCorrente("004", "Corrente", 2000.0, 1000.0, True)


conta1.deposita(500.0)
conta1.saca(200.0)
conta1.transfere_para(conta2, 300.0)

conta2.deposita(200.0)
conta2.saca(100.0)

conta_poupanca.calcular_juros_mensal(0.5)

conta_corrente.utilizar_cheque_especial(300.0)


conta1.obter_extrato()
conta2.obter_extrato()
conta_poupanca.obter_extrato()
conta_corrente.obter_extrato()
