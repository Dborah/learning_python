class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def depositar(self, quantidade):
        if quantidade > 0:
            self.saldo  += quantidade
        else:
            print("Erro no deposito")

    def consultar_saldo(self):
        return self.saldo

    def sacar(self, quantidade):
        if self.saldo - quantidade < self.limite:
            print('saldo insuficiente')
        else:
            self.saldo -= quantidade