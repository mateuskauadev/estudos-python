# Exercicio :
# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

nome = input("Digite seu nome: ")

nota = []

for i in range (1,8):
     voto = float(input("Digite a nota: "))
     nota.append(voto)

maior = max(nota)
menor = min(nota)
soma = sum(nota) - maior - menor
media = soma / 5

print()
print("Resultado Final:")
print(f"Nome: {nome}")
print(f"Melhor nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Media: {media:.4f}")
