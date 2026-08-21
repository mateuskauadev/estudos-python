# Exercicio: 
# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

n = int(input("Digite um numero inteiro positivo:"))

n_invertido = 0

while n > 0 :
     digito = n % 10 
     n_invertido = (n_invertido * 10) + digito
     n = n // 10

print(f"O numero invertido é {n_invertido}.")