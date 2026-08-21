#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de #15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

print("Digite o seu salário: ")

sal = float(input())


if sal <= 280 :
    sal_novo = (sal * 0.2) + sal
elif sal > 280 and sal <= 700:
    sal_novo= (sal * 0.15) + sal
else:
     if sal > 700 and sal < 1500:
        sal_novo = (sal * 0.10) + sal
     else: 
        sal_novo = (sal * 0.05) + sal

percentual = ((sal_novo - sal) / 100)

valor = sal_novo - sal

print(f"Salario antes do reajuste: {sal}")
print(f"Percentual aumentado: {percentual}")
print(f"Valor aumentado: {valor}")
print(f"Salario novo: {sal_novo}")