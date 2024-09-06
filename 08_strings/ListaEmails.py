#!python3

"""
  Criar um programa que prepare uma lista de emails para uma mala direta. O programa deverá armazenar
  as linhas abaixo num vetor, extrair de cada linha o email e armazenar num outro vetor. O programa
  deverá mostrar na tela a lista de email processada.

    Beltrano da Silva;beltrano@gmail.com
    Siclano Goncalves;siclano@yahoo.com.br
    Fulano Pereira Alves;fulanoalves@gmail.com
    Alvarenga Pedroso;pedroso@hotmail.com
"""

print("Lista de emails para mala direta")
print()

dados = [
  "Beltrano da Silva;beltrano@gmail.com", 
  "Siclano Goncalves;siclano@yahoo.com.br", 
  "Fulano Pereira Alves;fulanoalves@gmail.com", 
  "Alvarenga Pedroso;pedroso@hotmail.com"
]

emails = []

for linha in dados:
  posicaoDoCorte = linha.find(";") + 1
  emails.append(linha[posicaoDoCorte:])

for email in emails:
  print(email)
