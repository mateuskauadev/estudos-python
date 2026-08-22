# Exercicio: 
#Faça um programa para imprimir:
#1
#1   2
#1   2   3
#.....
#1   2   3   ...  n
#Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha.

def imprimir_padrao(n):
    for i in range(1, n + 1):
        for j in range (1, 1 + i):
           print(f"{j} ", end="")
        print()

n = int(input("Digite um valor para n: "))
imprimir_padrao(n)
