# Software de gestão para locadora de carros

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
 
def portifolio():
    print("[ PORTIFÓLIO DE CARROS DISPONÍVEIS ]")
    print()
    for i in range(len(lista_carro)):
        if lista_status[i] == True:
            print(f"[{i}] {lista_carro[i]} - R$ {lista_valores[i]} /dia")

def calculador(codigo, d):
    if codigo == 0:
        t = 120 * d
    elif codigo == 1:
        t = 90 * d
    elif codigo == 2:
        t = 150 * d
    elif codigo == 3:
        t = 85 * d
    elif codigo == 4:
        t = 120 * d
    elif codigo == 5:
        t = 60 * d
    elif codigo == 6:
        t = 70 * d
    elif codigo == 7:
        t = 130 * d
    else:
        print("Comando Inválido!")
        t = 0
    return t

def alugar():
    print("[ ALUGAR ] Dê uma olhada em nosso portifólio.")
    print()
    
    carros_disponiveis = False
    for i in range(len(lista_carro)):
        if lista_status[i] == True:
            print(f"[{i}] {lista_carro[i]} - R$ {lista_valores[i]} /dia")
            carros_disponiveis = True
            
    if not carros_disponiveis:
        print("Desculpe, todos os carros estão alugados no momento!")
        return

    print()
    print("=======")
    print("Escolha o código do carro:")
    codigo = int(input())
    
    if codigo < 0 or codigo >= len(lista_carro) or lista_status[codigo] == False:
        print("Código inválido ou carro já alugado!")
        return

    print("Escolha por quantos dias deseja alugar:")
    d = int(input())
    limpar_tela()
    
    print(f"Você escolheu {lista_carro[codigo]} por {d} dias.")
    total = calculador(codigo, d)
    print(f"O aluguel totalizaria R$ {total}. Deseja alugar?")
    print("0 - Sim | 1 - Não ")
    confirmacao = int(input())
    
    if confirmacao == 0:
        lista_status[codigo] = False
        print(f"\nParabéns! Você alugou o {lista_carro[codigo]} por {d} dias.")

def devolver():
    print("[ DEVOLVER ] Veja os carros que estão alugados com você:")
    print()
    
    carros_alugados = False
    for i in range(len(lista_carro)):
        if lista_status[i] == False:
            print(f"[{i}] {lista_carro[i]}")
            carros_alugados = True
            
    if not carros_alugados:
        print("Você não tem nenhum carro alugado no momento!")
        return

    print()
    print("=======")
    print("Escolha o código do carro que deseja devolver:")
    codigo = int(input())
    
    if codigo < 0 or codigo >= len(lista_carro) or lista_status[codigo] == True:
        print("Código inválido!")
        return
        
    lista_status[codigo] = True
    print(f"\nObrigado! O carro {lista_carro[codigo]} foi devolvido com sucesso.")

lista_carro = ["Chevrolet Tracker", "Chevrolet Onix", "Chevrolet Spin", "Hyundai HB20", "Hyundai Tucson", "Fiat Uno", "Fiat Mobi", "Fiat Pulse"]
lista_valores = [120, 90, 150, 85, 120, 60, 70, 130]
lista_status = [True, True, True, True, True, True, True, True]

continuar = 0

while continuar == 0:
    limpar_tela()
    print("=======")
    print("Bem vindo à locadora de carros!")
    print("=======")

    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    c = int(input())

    limpar_tela()

    if c == 0:
        portifolio()
    elif c == 1:
        alugar()
    elif c == 2:
        devolver()
    else:
        print("Comando Inválido!")

    print("\n============")
    print("0 - Continuar | 1 - Sair")
    continuar = int(input())