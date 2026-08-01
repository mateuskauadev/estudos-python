# O otimizador de Lotes (Batch Size para Treinamento de Modelos)
print("Digite as seguintes informações para nos podermos concluir a nossa pesquisa.")

# variaveis e contas
total_de_imagens = float(input("Digite o total de imagens do banco de dados: "))
tamanho_do_lote = float(input("Digite o tamanho do lote: ")) 

lotes_completos = total_de_imagens // tamanho_do_lote
ultimo_lote = total_de_imagens % tamanho_do_lote

#true e falso
tem_lote_incompleto = (ultimo_lote > 0)

print(f"lotes completos enviados : {lotes_completos}")
print(f"Tamanho do último lote restante: {ultimo_lote}")
print(f"Sobrou lote incompleto? {tem_lote_incompleto}")
