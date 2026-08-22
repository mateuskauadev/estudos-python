# Exercicio:
# Faça um programa que converta a notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
#Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas às vezes que desejar.

A = "A.M"
P = "P.M"

def descobrindo_o_periodo (horas):
    if horas == 0 or horas < 12:
       inform = A
    else:
       inform = P
    return inform



   
def convert (horas):
    if horas == 0:
      notacao = 12
    elif horas >= 13:
      notacao = horas - 12
    else:
      notacao = horas
    return notacao

continuar = "S"

while continuar == "S":
     horas = int(input("Digite as horas (0-23): "))
     minutos = int(input("Digite os minuts (0-59):"))

     periodo = descobrindo_o_periodo(horas)
     hora_convertida = convert(horas)

     print(f"São {hora_convertida}:{minutos:02d} {periodo}")
     continuar = input("Deseja continuar (S/N): ").upper()
    

       
    

