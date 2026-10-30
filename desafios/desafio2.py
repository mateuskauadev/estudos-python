#1 Quantas entregas atrasaram (atraso maior que 0);
#2 Qual foi o maior atraso;
#3 A média de atraso só entre as que atrasaram;
#4 A porcentagem de entregas atrasadas.



atrasos = [0, 3, 0, 5, 1]

i = 0
c = 0
maior = 0
s = 0

while i <= 4:
    if atrasos[i] > 0:
       c = c + 1
       s = s + atrasos[i]

    if atrasos[i] >= maior:
        maior = atrasos[i] 

    i = i + 1

media = s / c
porcentagem = (c / i) * 100
print(f"entregas atrasadas: {c}")
print(f"maior atraso: {maior}")
print(f"média: {media}")
print(f"porcentagem : {porcentagem}%")
    
