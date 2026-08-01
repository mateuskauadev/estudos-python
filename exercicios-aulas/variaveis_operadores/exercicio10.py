# Simulador de Economia de Energia em Clusters de GPU
print("Para simurlamos o consumo de energia precisaremos de alguns dados.")

# Variaveis e contas
quant_gpus = int(input("A quantidade de GPUs ativas no cluster: "))
consumo = float(input("O consumo de uma única GPU em Watts por hora: "))
tempo_m = int(input("O tempo total de treino do modelo em Minutos: "))

tempo_h = tempo_m / 60
watts_totais = tempo_h * consumo * quant_gpus
consumo_kwh = watts_totais / 1000

print(f"O consumo total em kwh sera de {consumo_kwh}")