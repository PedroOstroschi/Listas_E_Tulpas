class Conta_Corrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        try:
            self.saldo += valor
        except:
            raise ValueError("Valor inválido")

    def __str__(self):
        return "Código: {} \nSaldo: {}".format(self.codigo, self.saldo)



conta = Conta_Corrente("001")
conta.deposita(1000)

print(conta)