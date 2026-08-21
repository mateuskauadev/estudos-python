# Exercicio:
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

print("Digite uma nota entre 0 e 10")
nota = float(input())

while nota > 10 :
    print("Nota inválida! Digite uma nova nota:")
    nota = float(input())
print(f"nota: {nota}")