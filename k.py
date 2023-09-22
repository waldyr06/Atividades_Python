produto = []
preço = []
quantidade = []

concluir = False

while (not concluir):
    print("Digite o nome do produto: ")
    nomeProduto = input()
    print("Digite o preço do produto: ")
    preçoProduto = float(input())
    print("Digite a quantidade do produto: ")
    quantidadeProduto = int(input())
    
    produto.append(nomeProduto)
    preço.append(preçoProduto)
    quantidade.append(quantidadeProduto)

    print("Deseja incluir outro produto? (s/n)... ")
    concluir = input() == "n"

input("pressione ENTER para continuar")


# Escrever nomes em um arquivo

filename = "meuArquivo.txt"
file = open(filename, 'w')
for o in produto:
    outputline = f"Nome: {o}\n Preco: R${preço[produto.index(o)]}\n Quantidade: {quantidade[produto.index(o)]}\n \n"
    file.write(outputline)
file.close()

import os

os.system(f"notepad {filename}")
