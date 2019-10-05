'''
EXERCICIO:
Faça um programa que leia a quatidade de pessoas que serão convidadas para uma festa Após isso p programa irá perguntar
o nome de todas as pessoas e  colocar em uma lista de convidas. Imprimir a lista no final
'''

print('----- Convidados para a festa ------')

#pergunta quantas pessoas serão convidadas
numero_convidados = int(input('Informe quantas pessoas serão convidadas: '))

#lista de convidados
lista_convidados = []

#pergunta o nome de cada convidado
i = 1
while i <= numero_convidados:
    nome = input('Informe o nome do convidado: ')
    lista_convidados.append(nome)
    i += 1


print('\n-----3Lista de convidados-----')
#imprime os nomes dos convidados
for convidado in lista_convidados:
    print(convidado)