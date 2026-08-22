# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma_argumentos(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))
n3 = float(input("Digite um numero: "))

resultado =soma_argumentos(n1, n2, n3)

print(f"Soma = {resultado}")