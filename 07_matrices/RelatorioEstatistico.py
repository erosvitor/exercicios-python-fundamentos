#!python3

"""
  Os dados abaixo representam um levantamento realizado por uma prefeitura de uma determinada cidade.
  A primeira coluna é o salário e a segunda coluna representa a quantidade de filhos.

    1450.40, 1
    2630.00, 2
    970.00, 2
    1790.30, 1
    2150.10, 3
    1080.00, 2
    1920.60, 2
    2530.80, 3

  Com base nos dados acima a prefeitura deseja um relatório que contenha as seguintes informações:

    a) Média do salário da população
    b) Média do número de filhos
    c) Maior salário
"""

print("Relatório Estatístico")
print("")

dados = [ [1450.40, 1],
          [2630.00, 2],
          [970.00, 2],
          [1790.30, 1],
          [2150.10, 3],
          [1080.00, 2],
          [1920.60, 2],
          [2530.80, 3]]

totalSalarios = 0.0
totalNumeroFilhos = 0.0
maiorSalario = 0.0

for linha in dados:
  totalSalarios += linha[0]
  totalNumeroFilhos += linha[1]
  if linha[0] > maiorSalario:
    maiorSalario = linha[0]

salarioMedio = totalSalarios / len(dados)
print("O salário médio é de: ", salarioMedio)

mediaQtdeFilhos = totalNumeroFilhos / len(dados)
print("A quantidade média de filhos é: ", mediaQtdeFilhos)

print("O maior salário é: ", maiorSalario)
