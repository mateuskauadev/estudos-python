import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def resultado(ve, vj, vc):
    if ve == 1:
      resposta = "Você empatou!"
    elif vj == 1:
      resposta = "Você ganhou!"
    elif vc == 1:
      resposta = "Você perdeu!"
    return resposta

def decisao(j, c):
    ve = 0
    vj = 0
    vc = 0
    if j == 0 and c == 0:
        ve = 1
    elif j == 0 and c == 1:
        vj = 1
    elif j == 0 and c == 2:
        vc = 1
    elif j == 1 and c == 0:
        vc = 1
    elif j == 1 and c == 1:
        ve = 1
    elif j == 1 and c == 2:
        vj = 1
    elif j ==2 and c == 0:
        vj = 1
    elif j == 2 and c == 1:
        vc = 1
    elif j == 2 and c == 2: 
        ve = 1
    return ve, vj, vc
        
def jogador(j):
    if j == 0:
        n_jogador = "Papel"
    elif j == 1:
        n_jogador = "Pedra"
    elif j == 2:
        n_jogador = "Tesoura"
    else:
        print("Comando Inválido!")
    return n_jogador

import random
def computador():
    c = random.randint(0, 2)
    if c == 0:
        n_computador = "Papel"
    elif c == 1:
        n_computador = "Pedra"
    else:
        n_computador = "Tesoura"
    return c, n_computador

continuar = "S"
voce = 0
comp = 0
while continuar == "S":
    limpar_tela()
    print("===============================================")
    print("Bem vindo ao jogo do Papel, Pedra ou tesoura")
    print("===============================================")
    print()
    print("---- PLACAR ----")
    print(f"Você: {voce}")
    print(f"Computador: {comp}")
    print()
    print("Escollha seu lance:")
    print("0 - Papel | 1 - Pedra | 2 - tesoura")
    try:
        j = int(input())
        if j not in [0, 1, 2]:
            print("Número inválido! Escolha apenas 0, 1 ou 2.")
            input("\nAperte Enter para tentar de novo...")
            continue
    except ValueError:
        print("Entrada inválida! Digite apenas o NÚMERO (0, 1 ou 2), não digite letras.")
        input("\nAperte Enter para tentar de novo...")
        continue

    jogada_Jogador = jogador(j)
    c, jogada_computador = computador()
    ve, vj, vc = decisao(j, c)   

    if vj == 1:
        voce += 1
    elif vc == 1:
        comp += 1

    print("================")
    print(f"Sua Jogada: {jogada_Jogador}")
    print(f"Jogada do computador: {jogada_computador}")
    print(resultado(ve, vj, vc) )
    continuar= input("Quer continuar (S/N): ").upper()
