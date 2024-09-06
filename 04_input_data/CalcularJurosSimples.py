#!python3

"""
  Escreva um programa que calcule o juros simples sobre um determinado valor. A fórmula para calcular
  simples simples é a seguinte:

    J = C x I x N

    onde:
      J = juros calculado
      C = capital
      I = taxa
      N = período

      Obs.: Considerar taxa mensal e o período em meses.
"""

print("Calcular Juros Simples")
print("")

capital = input("Digite o capital: ")
taxa = input("Digite a taxa de juros (mensal): ")
periodo = input("Digite o período (em meses): ")

juros = float(capital) * (float(taxa)/100) * int(periodo)
print("O juros calculado foi de ", juros)
