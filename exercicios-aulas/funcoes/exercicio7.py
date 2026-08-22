# Exercicio:
# faça um programa que use a função valor_pagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valor_pagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução, o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento, o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valor_pagamento(valor, d):
    if d > 0:
        multa = valor * 0.03
        juros = valor * 0.001 * d
        total = valor + multa + juros
    else:
        total = valor
    return total

quantidade_pagas = 0
valor_total_do_dia = 0

while True:
   valor = float(input("Digite o valor da parcela (digite 0 para parar): "))
   if valor == 0:
        break
   atraso = input("Você tem prestação atrasada(S/N)? ").upper()
   if atraso == "S":
      d = int(input("Digite a quantidade de dias em atraso: "))
   else:
       d = 0
   valor_total = valor_pagamento(valor, d)

   print(f"O valor a ser pago é de R${valor_total:.2f}")
   continuar = input("Deseja continuar(S/N)").upper()
   quantidade_pagas = quantidade_pagas + 1
   valor_total_do_dia = valor_total_do_dia + valor_final_parcela

print("\n=== RELATÓRIO DO DIA ===")
print(f"Quantidade de prestações pagas: {quantidade_pagas}")
print(f"Valor total pago no dia: R$ {valor_total_do_dia:.2f}")

   
     
