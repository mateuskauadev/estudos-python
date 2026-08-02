#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

print("Me diga a suas notas e direi se voce passou direto.")

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
m = (n1 + n2) / 2

print(f"Sua media foi de {m:.3f} pontos.")

if m >= 7 and m < 10 :
    print("Você foi aprovado.")
elif m == 10 :
    print("Você foi aprovado com distinção.")
else:
    print("Você foi reprovado.")
