#!python3

"""
  Escreva um programa que mostre a situação escolar de um determinado aluno. O programa deverá
  solicitar ao usuário quatro notas bimestrais e depois mostrar se o aluno foi aprovado, reprovado ou
  recuperação. Se média for igual ou maior do que 70.0, mostrar APROVADO. Se a média for igual ou maior
  do que 40.0, mostrar EM RECUPERAÇÃO. Caso seja menor do que 40.0, mostrar REPROVADO.
"""

print("Verificar a situção escolar de um aluno")
print("")

nota1 = input("Digite a nota do primeiro bimestre: ")
nota1 = float(nota1)
nota2 = input("Digite a nota do segundo bimestre: ")
nota2 = float(nota2)
nota3 = input("Digite a nota do terceiro bimestre: ")
nota3 = float(nota3)
nota4 = input("Digite a nota do quarto bimestre: ")
nota4 = float(nota4)

media = (nota1+nota2+nota3+nota4) / 4

if media >= 70.0:
  print("O aluno esta aprovado")
elif media < 40.0:
  print("O aluno esta reprovado")
else:
  print("O aluno esta em recuperação")
