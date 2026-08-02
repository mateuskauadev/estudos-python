# Normalização de Dados Min-Max (Preparando Dados para a IA)
print("Para podermos fazer a nossa normalização de dados, precisaremos de algumas informações.")

# contas e variaveis
x = float(input("Digite o valor atual: "))
min = float(input("Digite o valor minimo: "))
max = float(input("Digite o valor máximo: "))

v_normalizado = (x - min) / (max - min)

# resultado
print(f"O valor normalizado sera de {v_normalizado:.4f}.")