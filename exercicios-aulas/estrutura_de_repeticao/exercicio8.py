# Exercicio : 
# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série


n = int(input("Digite a quantidade de numeros que voce deseja ver: "))

s = 0
denominador = 1

print("n termos da serie")

for numerador in range(1 , n + 1):
    termo_atual = numerador / denominador
    s = s + termo_atual

    if numerador < n:
        print(f"{numerador}/{denominador} +")
    else:
        print(f"{numerador}/{denominador}")

    denominador = denominador + 2
print(f" A soma é de {s}.")