#!python3

"""
  Criar um programa que leia o nome e a idade de 3 pessoas, guardando-os numa matriz e depois mostre
  o nome da pessoa mais velha.
"""

print("Pessoa mais velha")
print("")

pessoas = []

for i in range(0,3):
  nome = input(f"Digite o nome da pessoa {i+1}: ")
  idade = input(f"Digite a idade da pessoa {i+1}: ")
  pessoas.append([nome, int(idade)])

idadePessoaMaisVelha = 0
nomePessoaMaisVelha = ""

for pessoa in pessoas:
  if pessoa[1] > idadePessoaMaisVelha:
    idadePessoaMaisVelha = pessoa[1]
    nomePessoaMaisVelha = pessoa[0]

print("A pessoa mais velha é ", nomePessoaMaisVelha)
