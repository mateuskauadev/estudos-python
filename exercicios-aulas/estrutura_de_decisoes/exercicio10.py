#Faça um programa que pergunte em que turno você estuda. Peça para digitar:
#M - Matutino
#V - Vespertino
#N - Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou  "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Digite em qual turno você estuda (M: Matutino, V:Vespertino, N:Noturno): ")

turno = input()
turno = turno.upper()

if turno == "M":
   print("Bom dia!")
elif turno == "V":
   print("Boa tarde!")
else:
   if turno == "N":
       print("Boa noite!")
   else:
       print("Valor Inválido!")
