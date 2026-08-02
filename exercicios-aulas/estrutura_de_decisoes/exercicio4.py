#Faça um programa que verifique se uma letra digitada é vogal ou consoante.

print("Digite uma letra e verificaremos se ela é consoante ou volgal.")

consoante = ["A", "E", "I", "O", "U"]
n = input()
n = n.upper()

if n in consoante:
   print("A letra digitada é uma vogal.")
else:
   print("A letra digitada é uma consoante")
   
