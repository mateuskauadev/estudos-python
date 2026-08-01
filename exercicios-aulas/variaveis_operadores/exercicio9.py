# Codificador One-Hot Inteligente (Transformando Texto em Números)

#variaveis
categoria = input("Digite a categoria (gato, cachorrou ou passaro):")

gato_booleano = (categoria == "gato")
cachorro_booleano = (categoria == "cachorro") 
passaro_booleano = (categoria == "pássaro")

e_gato = int(gato_booleano)
e_cachorro = int(cachorro_booleano) 
e_passaro = int(passaro_booleano)

print(f"Vetor One-Hot: {e_gato} {e_cachorro} {e_passaro}.")