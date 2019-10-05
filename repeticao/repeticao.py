nomes = ['Ana', 'Claudia', 'Bruna', 'Julia']
frutas = ['maça', 'pera', 'uva', 'abacaxi', 'goiaba']

for nome in nomes:
    print(nome)

# for até 100 com intervalo de 20
for i in range(0, 100, 20):
    print(i)

for i in range(len(nomes)):
    print(nomes [i])
    nomes.append(' silva')
print(nomes)


#usando while
i = 0
while i < 10:
    print(i, 'ainda é menor do que 10')
    i += 1


contador = 0
numero = 0

for fruta in frutas:
    contador += 1
print(contador)

#usando break
while True:
    print(numero)
    if(numero == 3):
        break
    numero += 1