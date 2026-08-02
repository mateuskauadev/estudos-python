# Cálculo de Custo de Armazenamento em Nuvem (AWS)
print("Digite a quantidade de dados que o modelo de IA usa em Terabytes (TB):")

#variaveis e calculos
q_tb = float(input())
q_gb = q_tb * 1024
custo = q_gb * 12 * 0.15

print(f"A quantidade armazenada de Gigabyte (GB) ao mês sera de {q_gb} GB.")
print(f"O custo total de armazenamento em reais para um período de 12 meses sera de R${custo:.2f}")