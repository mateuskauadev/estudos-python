# PARTE 1: GRAVAR OS PEDIDOS
with open("pedidos.txt", "w", encoding="utf-8") as arquivo:
    for i in range(3):
        cliente = input(f"Cliente do pedido {i + 1}: ")

        while True:
            try:
                valor = float(input("Valor: "))
            except ValueError:
                print("Digite só números!")
                continue
            if valor <= 0:
                print("O valor tem que ser maior que zero!")
                continue
            break

        arquivo.write(f"{cliente};{valor}\n")

print("Pedidos salvos!")

# PARTE 2: LER O ARQUIVO E SOMAR
print("\nLendo o arquivo...")
total = 0

try:
    with open("pedidos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(";")
            cliente = partes[0]
            valor = float(partes[1])
            print(f"{cliente}: R$ {valor:.2f}")
            total = total + valor
    print(f"Total vendido: R$ {total:.2f}")
except FileNotFoundError:
    print("Nenhum pedido encontrado.")