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




julia = Conta_Corrente(13)
pedro = Conta_Corrente(42)

contas = (julia, pedro)
julia.deposita(1000)
for conta in contas:
    print(conta)