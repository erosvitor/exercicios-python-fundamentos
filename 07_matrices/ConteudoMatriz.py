#!python3

"""
  Escreva um programa que leia 4 números inteiros e guarde-os numa matriz 2x2. Depois da leitura dos
  números, mostrar na tela o conteúdo da matriz.
"""

print("Mostra conteúdo de uma matriz")
print("")

matriz = []

for i in range(0, 2):
  linha = []
  for j in range(0,2):
    valor = input(f"Digite o elemento para a posição {i},{j} da matriz: ")
    linha.append(int(valor))
  matriz.append(linha)

for linha in matriz:
  for item in linha:
    print(item)
