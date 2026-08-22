# Exercicio:
# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# 8  3  4
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

import itertools

def eh_quadrado_magico(q):

    soma_linhas = (q[0]+q[1]+q[2] == 15 and 
                   q[3]+q[4]+q[5] == 15 and 
                   q[6]+q[7]+q[8] == 15)
                   
    soma_colunas = (q[0]+q[3]+q[6] == 15 and 
                    q[1]+q[4]+q[7] == 15 and 
                    q[2]+q[5]+q[8] == 15)
                    
    soma_diagonais = (q[0]+q[4]+q[8] == 15 and  
                      q[2]+q[4]+q[6] == 15)     

    
    return soma_linhas and soma_colunas and soma_diagonais

def encontrar_quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    contador = 0

   
    for combinacao in itertools.permutations(numeros):
        if eh_quadrado_magico(combinacao):
            contador = contador + 1
            print(f"--- Quadrado Mágico nº {contador} ---")
            print(f"{combinacao[0]}  {combinacao[1]}  {combinacao[2]}")
            print(f"{combinacao[3]}  {combinacao[4]}  {combinacao[5]}")
            print(f"{combinacao[6]}  {combinacao[7]}  {combinacao[8]}")
            print() 


encontrar_quadrados_magicos()