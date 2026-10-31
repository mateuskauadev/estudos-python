def calcular_frete(p, d):
    frete = p * 0.5 + d * 2

    if frete < 50:
        frete = 50

    return frete
     


i = 1
peso = []
distancia = []

while i <= 2:
    peso.append(float(input(f"\n[Caminhão {i}] Digite o peso: ")))
    distancia.append(float(input(f"[Caminhão {i}] Digite a distancia: ")))

    frete = calcular_frete(peso[i - 1], distancia[i - 1])

    print(f"frete {i}: {frete}")
    i = i + 1
