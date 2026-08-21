# Exercicio:
#Faça um programa que leia e valide as seguintes informações:                                    Nome: maior que 3 caracteres;                   Idade: entre 0 e 150;                        Salário: maior que zero;                          Estado Civil: 's', 'c', 'v', 'd';

print("Digite as seguintes informações que iremos fazer seu cadastro.")

lista_estado = ["S", "C", "V", "D"]

nome = input("Digite seu nome: ")
idade = float("Digite sua idade: ")
salario = float("Digite seu salario: ")
estado = input("Digite seu estado civil(S, C, V, D): ")
estado = estado.upper()
tam = len(nome)

while tam <= 3 or idade < 0 or idade > 150 or salario <= 0 or estado not in lista_estado:
   print("Erro!")
   nome = input("Digite seu nome: ")
   idade = float("Digite sua idade: ")
   salario = float("Digite seu salario: ")
   estado = input("Digite seu estado civil(S, C, V, D): ")
   estado = estado.upper()
   tam = len(nome)
print("Informações salvas!")