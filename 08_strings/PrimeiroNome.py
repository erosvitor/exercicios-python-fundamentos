#!python3

"""
  Criar um programa que solicite o nome completo do usuário e depois mostre na tela o primeiro nome do
  usuário.
"""

print("Primeiro nome")
print("")

nomeCompleto = input("Digite seu nome completo: ")
primeiroNome = nomeCompleto[0: nomeCompleto.find(" ")]

print("Seu primeiro nome é ", primeiroNome)
