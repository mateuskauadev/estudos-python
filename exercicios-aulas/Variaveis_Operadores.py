print("--------------------------------------------")
print("    Exercícios: Variáveis e Operações     ")
print("--------------------------------------------")
# Exercício 1: Identidade do Desenvolvedor

print("Iremos fazer uma rapida análise sobre seu perfil, digite os dados a seguir.")
# Variaveis
nome = input("Nome: ")
idade = int(input("Idade: "))
profissao = input("Profissão: ")
print(F"Seu nome é {nome}, você tem {idade} anos e você é {profissao}.")

# Exercício 2: Calculadora de Hardware

print("Iremos calcular quanto de espaço você tem.")
# Variaves e calculos
espaco_total = 16
espaco_gasto = int(input("Digite o quanto você gastou: "))
espaco_livre = 16 - espaco_gasto
print(f"Você tem {espaco_livre} GB livres.")


# Exercício 3: Media

print("Digite suas notas para podermos calcular sua média.")
# Variaves e calculos
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
media = (nota1 + nota2)  / 2
print(f"Você ficou com uma media de {media} pontos.")


# Exercício 5: A Distância Euclidiana

print("Iremos calcular a Distância Euclidiana, mas para isso precisaremos das coordenadas dos dois pontos.")
# Variaveis e calculos
xi = float(input("Digite o x inicial:"))
yi = float(input("Digite o y inicial: "))
xf = float(input("Digite o x final: "))
yf = float(input("Digite o y final: "))
dx = xf - xi
dy = yf - yi
distancia = (dx**2 + dy**2) ** 0.5
print(f"A distância entro os dois pontos sera de {distancia} metros. ")

# Exercício 6: A Função de Ativação ReLU


