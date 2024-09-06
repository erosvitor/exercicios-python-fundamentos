#!python3

"""
  Utilizando a estrutura de repetição FOR, escreva um programa que mostre na tela os números divisíveis
  por 3 que estão entre os números de 0 e 100.
"""

print("Números divisíveis por 3 entre 0 e 100")
print("")

for numero in range(0,101):
  if numero % 3 == 0:
    print(numero)

