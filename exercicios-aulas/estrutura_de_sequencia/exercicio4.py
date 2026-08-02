# Exercício 4: A Distância Euclidiana

print("Iremos calcular a Distância Euclidiana, mas para isso precisaremos das coordenadas dos dois pontos.")

# Variaveis e calculos
xi = float(input("Digite o x inicial:"))
yi = float(input("Digite o y inicial: "))
xf = float(input("Digite o x final: "))
yf = float(input("Digite o y final: "))

# calculos
dx = xf - xi
dy = yf - yi
distancia = (dx**2 + dy**2) ** 0.5

print(f"A distância entro os dois pontos sera de {distancia} metros. ")