# exercicio:
# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = int(input("Digite a quantidade de Termos: "))

h = 0

for denominador in range (1, n +1):
 termo = 1 / denominador
 h = h + termo

print(f"A soma é {h:.4f}.")