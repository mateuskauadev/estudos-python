# Exercicio:
# Faça um programa com uma função chamada soma_imposto. A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas expressas em porcentagem, e custo, que é o custo de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas.


def soma_imposto(taxa_imposto, custo):
    imposto_pago = custo * (taxa_imposto / 100)
    custo_com_imposto = imposto_pago + custo

    return custo_com_imposto

taxa_imposto = float(input("Digite o valor em porcentagem sem o %: "))
custo = float(input("Digite o custo de fabricação: "))

preco = soma_imposto(taxa_imposto, custo)

print(preco)
