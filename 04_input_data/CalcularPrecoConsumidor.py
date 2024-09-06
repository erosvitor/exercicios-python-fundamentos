#!python3

"""
  O preço consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor
  e dos impostos (aplicados ao custo de fábrica). Supondo que a porcentagem do distribuidor seja de
  28% e os impostos sobre o custo de fábrica seja de 45%, crie um programa que leia o custo de
  fábrica de um determinado carro e depois mostre na tela o preço consumidor.
"""

print("Calcular preço consumidor")
print("")

porcentagemDistribuidor = 28/100
impostos = 45/100

custoFabrica = input("Informe o custo de fábrica: ")
custoFabrica = float(custoFabrica)

precoConsumidor = custoFabrica + (custoFabrica * porcentagemDistribuidor)
precoConsumidor = precoConsumidor + (precoConsumidor * impostos)
print("O preço consumidor é de ", precoConsumidor)

