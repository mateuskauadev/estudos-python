# Exercicio :
# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento for zero ou negativo.

def retornador(n):
    if n <= 0:
        arg = "N"
    else:
        arg = "P"
    return arg

n = float(input("Digite um valor para n: "))

resultado = retornador(n)

print(resultado)
    
    