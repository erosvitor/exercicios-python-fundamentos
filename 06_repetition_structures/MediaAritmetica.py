#!python3

"""
  Utilizando a estrutura de repetição WHILE, escreva um programa que solicite ao usuário quatro números
  inteiros e depois mostre na tela a média aritmética dos números informados.
"""

print("Média Aritmética")
print("")

qtde = 1
nota = 0.0

somaDasNotas = 0.0
while qtde <= 4:
  nota = input(f"Digite a nota {qtde}:")
  nota = float(nota)
  somaDasNotas += nota
  qtde += 1

media = somaDasNotas / 4

print(f"A média aritmética é {media}")
