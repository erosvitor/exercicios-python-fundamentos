#!python3

"""
  Utilizando a estrutura de repetição WHILE, escreva um programa que mostre na tela todos os números
  ímpares entre os números 0 e 100.
"""

print("Números ímpares entre 0 e 100")
print("")

numero = 0
while numero <= 100:
  if numero % 2 != 0:
    print(numero)
  numero += 1
