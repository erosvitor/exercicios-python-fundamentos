#!python3

"""
  Escreva um programa que armazene os números 1, 2, 3, 4, 5 e 6 num vetor e depois mostre os dados em
  ordem decrescente.
"""

print("Ordem decrescente")
print("")

numeros = [1, 2, 3, 4, 5, 6]

for i in range(5, -1, -1):
  print(numeros[i])
