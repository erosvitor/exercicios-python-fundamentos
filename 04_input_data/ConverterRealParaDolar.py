#!python3

"""
  Escreva um programa para converter a moeda Real para a moeda Dolar. O programa deve solicitar ao
  usuário um valor em reais e depois mostrar na tela o valor em dólares. Assumir como cotação do
  dolar o valor de 3,35.
"""

print("Converter reais para dólares")
print("")

cotacaoDolar = 5.28

reais = input("Digite um valor em reais: ")
dolares = float(reais) / cotacaoDolar

print(f"{reais} reais equivalem a {dolares} dolares")

