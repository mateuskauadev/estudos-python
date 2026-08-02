#Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino
#M - Masculino
#Sexo Inválido.

print("Digite qual o seu gênero. Escolha [M] para masculino e [F] para feminino")

genero = input()
genero = genero.upper()

if genero =="M" :
  print("Você é um homem.")
elif genero == "F":
  print("Você é uma mulher.")
else:
  print("Sexo Inválido.")
