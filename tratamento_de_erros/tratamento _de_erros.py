import time

#divisao por zero
try:
    a = 1200 / 0
except ZeroDivisionError as erro:
    print('aconteceu um erro: ', erro)


try:
    teste()
except Exception as erro:
    print('aconteceu um erro:', erro)



def abre_arquivo():
    try:
        arquivo = open('arquivo.txt')
        return True
    except Exception as erro:
        print("aconteceu erro erro:", erro)
        return False



while not abre_arquivo():
    print('tentando abrir o arquivo')
    time.sleep(5)

print('arquivo aberto')


