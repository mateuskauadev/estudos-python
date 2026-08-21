# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

print("Digite algumas informações.")
nome = input("Digite seu nome: ")
senha = input("Digite uma senha: ")

while nome == senha:
    print("Erro!")
    nome = input("Digite um novo nome: ")
    senha = input("Digite uma nova senha: ")
print("Senha salva!")
