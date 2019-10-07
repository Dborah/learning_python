from Cliente import Cliente
from Conta import Conta

cliente1 = Cliente('ana', '111.444.444-89', 27)


conta_ana = Conta(cliente1,10.50, 10000)
print(conta_ana.cliente.nome,conta_ana.consultar_saldo())

conta_ana.depositar(1000.40)
print(conta_ana.consultar_saldo())

conta_ana.sacar(500)
print(conta_ana.consultar_saldo())