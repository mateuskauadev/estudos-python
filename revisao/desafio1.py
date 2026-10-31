#1 pergunta a capacidade do caminhão em kg;
#2 pergunta o peso de 3 pacotes;
#3 mostra o peso total;
#4 diz se cabe (e quanto sobra) ou se passou da capacidade (e por quanto).

print("Digite a capacidade do caminhão em kg:")
capacidade = float(input())


i = 1
s = 0

while (i <= 3):
    print("Digite o peso do pacotes:")
    peso = float(input())
    s = s + peso
    i = i + 1

print(f"peso total: {s} kg")

if (s > capacidade):
    print("Caminhão não conseguirá transportar")
    passou = s - capacidade
    print(f"passou {passou} kg")
else:
    print("Caminhã ira carregar")
    sobra = capacidade - s
    print(f"Sobrou {sobra} kg")