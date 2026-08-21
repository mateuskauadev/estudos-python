# Exercicio:
# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

continuar = "S"
soma = 0 
n = 0
while continuar == "S": 
    idade = float(input("Digite sua idade: "))
    n = n + 1
    soma = soma + idade
    continuar = input("Deseja contuar (S / N): ").upper()

media = soma / n

if media >= 0 and media <= 25:
    turma = "Jovem"
elif media >= 26 and media <= 60:
    turma = "Adulto"
else:
    turma = "Idosa"

print(f"A turma é {turma} e a média é {media}")
