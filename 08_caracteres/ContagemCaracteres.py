#!python3

"""
  Criar um programa que leia um texto e depois mostre na tela a quantidade de caracteres excluindo os
  espaços em branco.
"""

print("Contagem de Caracteres")
print("")

texto = input("Digite um texto qualquer: ")

totalCaracteres = 0
for i in range(0, len(texto)):
  caractere = texto[i]
  if not caractere.isspace():
    totalCaracteres += 1

print(f"O texto informado possui {totalCaracteres} caracteres, excluindo os espaços em branco.")
