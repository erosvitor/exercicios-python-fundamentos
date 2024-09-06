#!python3

"""
  Utilizando a estrutura de repetição FOR, escreva um programa que solicite ao usuário um número
  inteiro e depois mostre na tela a tabuada do número informado no seguinte formato:

    N x 1 = Y
    N x 2 = Y
    ...
    N x 10 = Y

    onde:
      N é o número informado pelo usuário
      Y é o resultado da multiplicação
"""

print("Tabuada de um número")
print("")

numero = input("Digite um número inteiro entre 1 e 10: ")
numero = int(numero)

for i in range(1, 11):
  print(f"{numero} x {i} = {numero*i}")
