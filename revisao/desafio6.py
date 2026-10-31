def mapa_tabuleiro(tabuleiro):
    for i in range(3):
        for c in range(3):
            if c == 2:
                print(f" {tabuleiro[i][c]}")
            else:
                print(f" {tabuleiro[i][c]} |", end="")
        if i != 2:
            print("---+---+---")


def quem_venceu(tabuleiro):
    for jogador in ["x", "o"]:
        # linhas
        for i in range(3):
            if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
                return jogador
        # colunas
        for i in range(3):
            if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
                return jogador
        # diagonais
        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
            return jogador
        if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
            return jogador
    return None     # ninguém venceu


tabuleiro = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

jogador = "x"
jogadas = 0
vencedor = None

mapa_tabuleiro(tabuleiro)

while jogadas <= 8:
    while True:
        try:
            numero = int(input(f"Vez do {jogador}. Escolha uma casa (1-9): "))
        except ValueError:
            print("Erro! Digite só números.")
            continue

        if numero < 1 or numero > 9:
            print("Escolha um número de 1 a 9!")
            continue

        posicao = numero - 1
        linha = posicao // 3
        coluna = posicao % 3

        if tabuleiro[linha][coluna] == "x" or tabuleiro[linha][coluna] == "o":
            print("Casa ocupada! Escolha outra casa.")
            continue

        tabuleiro[linha][coluna] = jogador
        break

    mapa_tabuleiro(tabuleiro)

    vencedor = quem_venceu(tabuleiro)
    if vencedor != None:
        print(f"O jogador {vencedor} venceu!")
        break

    if jogador == "x":
        jogador = "o"
    else:
        jogador = "x"

    jogadas = jogadas + 1

if vencedor == None:
    print("Deu velha!")