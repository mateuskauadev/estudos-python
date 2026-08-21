# Faça um programa que leia três números e mostre o maior e o menor deles:

print("Digite tres numero para que possamos verificar qual o maior e qual o menor:")

n1 = float(input())
n2 = float(input())
n3 = float(input())

# Para n1 como o maior.
if n1 >= n2 and n1 >= n3:
   maior = n1
   if n2 >= n3:
      menor = n3
   else:
      menor = n2
# Para n2 como o maior
elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n1 >= n3:
       menor = n3
    else: 
       menor = n1
# Para n3 como maior
else:
    if n1 >= n2:
       menor = n2
    else:
       menor = n1
print(f"O maior sera {maior} e o menor sera{menor}.")