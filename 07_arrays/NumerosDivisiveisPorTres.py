#!python3

"""
  Escreva um programa que armazene os números 8, 6, 27, 13, 36 e 9 num vetor e depois mostre na tela
  os números que são divisíveis por 3.
"""

print("Números divisíveis por três")
print("")

numeros = [8, 6, 27, 13, 36, 9]

for num in numeros:
  if num % 3 == 0: 
    print(num)

