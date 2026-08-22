#calculadora

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def comando():
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite um outro numero: "))
    return n1, n2

def soma(n1,n2):
    som = n1 + n2
    print(f"{n1} + {n2} = {som}")

def subtração(n1,n2):
    sub = n1 - n2
    print(f"{n1} - {n2} = {sub}")

def multiplicação(n1,n2):
    mul = n1 * n2
    print(f"{n1} x {n2} = {mul}")
    
def divisao(n1,n2):
    if n2 == 0:
        print("Não é possivel dividir por zero!")
    else:
        div = n1 / n2
        print(f"{n1} / {n2} = {div}")

def exponenciação(n1,n2):
    exp = n1 ** n2
    print(f"{n1} ¨ {n2} = {exp}")

def estrutura(c):
        if c == 1:
            n1, n2 = comando()
            soma(n1,n2)
        elif c == 2:
            n1, n2 = comando()
            subtração(n1,n2)
        else:
            if c == 3:
               n1, n2 = comando()
               multiplicação(n1,n2)
            elif c == 4:
                n1, n2 = comando()
                divisao(n1,n2)
            else:
                if c == 5:
                   n1, n2 = comando()
                   exponenciação(n1,n2)
                else:
                   print("Comando inválido!")

continuar = "S" \
""
while continuar == "S":
    limpar_tela()
    print("--------- Calculadora ----------")
    print("       [1] Soma")
    print("       [2] Subtração")
    print("       [3] Multiplicação")
    print("       [4] Divisão")
    print("       [5] Exponenciação")
    print("--------------------------------")

    c = int(input("Escolha a oporação desejada: "))

    estrutura(c)

    input("\nPressione ENTER para continuar...")

    continuar = input("Deseja continuar (S/N): ").upper()