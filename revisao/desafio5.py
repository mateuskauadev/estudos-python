while True:
    try:
        peso = float(input("Digite o peso: "))   # só a linha perigosa
    except ValueError:
        print("Erro: Digite só números")         # roda SE deu erro
    else:
        if peso <= 0:                            # roda SE NÃO deu erro
            print("O peso não pode ser negativo nem zero!")
        else:
            print(f"Peso registrado: {peso} kg")
            break