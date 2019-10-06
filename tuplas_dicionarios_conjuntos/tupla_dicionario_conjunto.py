lista = ['ana', 'maria']  #mutável
tupla = ('ana', 'maria' ) #imutável(nao pode acrescentar ou retirar elementos)
dicionario = {'nome': 'ana', 'idade': 32}  # composto de chave e valor
conjunto = {'ana', 'maria'} # não pode itens repetidosu

print(tupla[0])

for nome in tupla:
    print(nome)

if 'ana' in tupla:
    print('Ana está na tupla')

#####################

print(dicionario)
print(dicionario['idade'])
print(len(dicionario))

if 'ana' in dicionario.values():
    print('ana está no dicionario')

for valores in dicionario.values():
    print(valores)

dicionario['idade'] = 56
print(dicionario)

dicionario['teledone'] = '8888-8888'
print(dicionario)
dicionario.clear()

#########################

print(conjunto)
conjunto.add('joao')
print(conjunto)

if 'ana' in conjunto:
    print('ana foi encontrada no conjunto')

conjunto.remove('joao')
print(conjunto)

####################
minha_lista = []
minha_tupla = ()
meu_dicionario = {}
meu_conjunto = set()

##################
