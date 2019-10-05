'''
Exercicio:
Faça um programa que pergunte a idade, o peso e altura de uma pessoa e decida se ela está apta a entrar no exercíto.
Para entrar o exercíto é preciso ter mais de 18 anos, pesar mais ou igual 60 kilos e medir mais ou igual  1,70 metros.
'''

print('------ CheckList do Exercíto-------\nMenu:\n')
idade = int(input('Informe sua idade:'))
peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Você está apto a servir o exercíto')
else:
    print('Você não está apto a servir o exercíto :/')

