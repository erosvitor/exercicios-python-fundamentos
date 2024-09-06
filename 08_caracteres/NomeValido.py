#!python3

"""
  Criar um programa para verificar se um nome de pessoa é um nome válido. Um nome válido para pessoa é
  aquele que contem apenas letras e espaços em branco.
"""

print("Nome válido")
print("")

nome = input("Digite o nome completo de uma pessoa: ")

nomeValido = True
for i in range(0, len(nome)):
  caractere = nome[i]
  if (not caractere.isalpha()) and (not caractere.isspace()):
    nomeValido = False
    break

if nomeValido:
  print("O nome informado é válido")
else:
  print("O nome informado é inválido")
