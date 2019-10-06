#biblioteca que permite comunicar com o SO
import sys

argumentos = sys.argv #arg1 = metodo - arg2 =  n1 - arg3 = n2

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if argumentos[1] == 'soma':
    resultado = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == 'sub':
    resultado = sub(float(argumentos[2]), float(argumentos[3]))

print(resultado)