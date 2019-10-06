def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

retorno = soma(75.34, 23.54)

def tem_sete_item(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False


print(tem_sete_item({1,2,3,4,5,6,7}))