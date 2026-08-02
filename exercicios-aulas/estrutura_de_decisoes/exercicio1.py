
#Faça um programa que peça dois números e imprima o maior deles.


print("Digite dois numeros e falaremos o maior entre eles.")

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um outro numero: "))

if n1 > n2 :
   print(f"o maior numero sera o primeiro numero: {n1}")
else:
   print(f"O maior numero sera o segundo numero: {n2}")