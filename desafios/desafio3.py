#1 pedir uma placa;
#2 se a placa não existir, mostrar Caminhão não encontrado;
#3 se existir, pedir o peso da carga e dizer se cabe (e quanto sobra) ou se passou (e por quanto).

frota = {"RJO1A23": 1000, "SPA4B56": 3000, "MGB7C89": 8000}

placa = input("digite uma placa: ")
placa = placa.upper()


if placa in frota: 
    print("Caminhão faz parte da frota")
    caminhao = frota[placa]
    peso = float(input("Digite o peso da carga: "))
    if caminhao >= peso:
       sobra = caminhao - peso
       print(f"A carga cabe dentro do caminhão e sobrou {sobra} kg")
    else:
       falto = peso - caminhao
       print(f"A carga não cabe no caminhão e passou {falto} kg acima do permitido")
        

else:
    print("Caminhão não encontrado")