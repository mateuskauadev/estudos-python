import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_tabuleiro(tabuleiro):
    for i in range(9):
        if (i + 1) % 3 == 0:
            print(tabuleiro[i])
            if i != 8:
                print("--+---+--")
        else:
            print(tabuleiro[i], end=" | ")


def fazer_jogada(tabuleiro, jogador):
    while True:
        entrada = input(f"Jogador {jogador}, escolha uma posição (1 a 9): ")

        if not entrada.isdigit() or int(entrada) < 1 or int(entrada) > 9:
            print("Digite um número de 1 a 9!")
        elif tabuleiro[int(entrada) - 1] in ["X", "O"]:
            print("Essa casa já está ocupada!")
        else:
            tabuleiro[int(entrada) - 1] = jogador
            break


def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ]

    for trinca in combinacoes:
        if tabuleiro[trinca[0]] == jogador and tabuleiro[trinca[1]] == jogador and tabuleiro[trinca[2]] == jogador:
            return True

    return False


tabuleiro = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

limpar_tela()
jogador = input("Quem começa, X ou O? ").strip().upper()

while jogador not in ["X", "O"]:
    print("Opção inválida!")
    jogador = input("Quem começa, X ou O? ").strip().upper()

jogadas = 0

while jogadas < 9:
    limpar_tela()
    mostrar_tabuleiro(tabuleiro)
    fazer_jogada(tabuleiro, jogador)
    jogadas += 1

    if verificar_vitoria(tabuleiro, jogador):
        limpar_tela()
        mostrar_tabuleiro(tabuleiro)
        print(f"Jogador {jogador} venceu!")
        break

    if jogadas == 9:
        limpar_tela()
        mostrar_tabuleiro(tabuleiro)
        print("Deu velha! Empate.")

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"