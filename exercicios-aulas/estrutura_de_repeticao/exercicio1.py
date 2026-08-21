# Exercicio:
# Produtos de até 1000 pagam 10% e produtos acima de 1000 pagam 15% de imposto

lista = [1000, 1500, 800, 2000]
imposto_total = 0

for preco in lista:
    if preco > 1000:
       taxa = 0.15
    else:
       taxa = 0.10
    imposto = preco * taxa
    imposto_total = imposto + imposto_total
print(f"O imposto total sobre os produtos comprados é de {imposto_total}")