import numpy as np
from functools import total_ordering

@total_ordering
class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        try:
            self._saldo += valor
        except:
            raise ValueError("Valor inválido")

    def __str__(self):
        return "Código: {} \nSaldo: {}".format(self._codigo, self._saldo)

    def __eq__(self, other):
        return self._codigo == other._codigo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

class Conta_Corrente(Conta):
    def __init__(self, codigo):
        super().__init__(codigo)

    def passa_o_mes(self):
        self._saldo -= 2

class Conta_Poupanca(Conta):
    def __init__(self, codigo):
        super().__init__(codigo)

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

np.array([1, 3.5])


julia = Conta_Poupanca(13)
pedro = Conta_Corrente(42)

julia.deposita(1000)
pedro.deposita(1000)
contas = (julia, pedro)

for conta in contas:
    conta.passa_o_mes()#duck typing
    print(conta)