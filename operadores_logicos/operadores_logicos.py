#Comparações:   ==   !=   <    >   >=   <=  and   or not

print("Menu:\n1 = EScreve João\n2- Escreve Maria\n3 - Escreve Ana\n")

opcao = input('Escolha uma opçao:')

if opcao == '1':
    print('João')
elif opcao == '2':
    print('Maria')
elif opcao == '3':
    print('Ana')
else:
    print('Opção inválida')

print(not True)
idade = 50
if  not idade == 50:
    print('voce mao tem 50 anos')
else:
    print('vc tem 50 anos')
