#open('arquivo.txt')              #leitura
#open('arquivo.txt', 'w')         #cria o arquivo
#open('arquivo.txt', 'r')         #leitura
#open('arquivo.txt', 'r+')        #leitura e escrita de arquivo
#open('arquivo.txt', 'a')         #escreve no final no arquivo
#open('arquivo.txt', 'b')         #abre arquivos que não são de texto


arquivo = open('arquivo.txt', 'r')

#escrevendo
#for i in range(1, 1001):
#    arquivo.write('numero: ' + str(i) + '\n')

#lendo
for linha in arquivo:
    print(linha)