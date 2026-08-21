# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:

print("Digite as seguintes informações e falarei qual você deve compar.")

# Variaveis
nome1 = input("Digite o nome do produto 1: ")
p1 = float(input("Digite o preço do produto 1: "))
nome2 = input("Digite o nome do produto 2: ")
p2 = float(input("Digite o preço do produto 2: "))
nome3 = input("Digite o nome do produto 3: ")
p3 = float(input("Digite o preço do produto 3: "))

# p1 maior

if p1 >= p2 and p1 >= p3:
   if p2 >= p3:
      menor = nome3
   else: 
      menor = nome2
# p2 maior
elif p2 >= p1 and p2 >= p3:
   if p1 >= p3:
      menor = nome3
   else: 
      menor = nome1
# p3 maior
else:
    if p1 >= p2:
      menor = nome2
    else:
      menor = nome1

print(f"O produto que voce deve comprar é o {menor}.")
