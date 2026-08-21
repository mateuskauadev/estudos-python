#Faça um programa que leia três números e mostre o maior deles

print("Digite três numeros e direi qual é o maior entre eles.")

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um outro numero: "))
n3 = float(input("Digite um outro numero: "))

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

print(f"O maior numero entre eles sera o {maior}.")