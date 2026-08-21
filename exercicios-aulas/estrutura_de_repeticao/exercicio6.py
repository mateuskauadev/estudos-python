# Exercicio:
# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

print("------- Eleição------")
print("nessa eleição temos os candidato A, B e C.")

n = float(input("Digite o numero de eleitores: "))
i = 0
va = 0
vb = 0
vc = 0
while i < n:
     voto = input("Digite o seu voto (A, B, C): ").upper()
     if voto == "A":
         va = va + 1
     elif voto == "B":
         vb = vb + 1
     else:
       if voto == "C":
          vc = vc + 1
       else:
          print("Erro! Digite uma opção válida.")
     i = i + 1

print(f"Candidato A: {va} votos")
print(f"Candidato B: {vb} votos")
print(f"Candidato C: {vc} votos")