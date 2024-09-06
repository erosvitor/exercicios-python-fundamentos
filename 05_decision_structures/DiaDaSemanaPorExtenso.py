#!python3

"""
  Escreva um programa que solicite um dia da semana (entre 1 a 7) e depois mostre o nome por extenso do
  dia informado. Caso o usuário informe um dia inválido, o programa deverá mostrar uma mensagem
  informando que o dia é inválido. Por exemplo, o usuário digitou o dia da semana 1, o programa deverá
  mostrar na tela 'Domingo'.
"""

print("Dia da semana por extenso")
print("")

diaSemana = input("Digite o dia da semana (1-7): ")
diaSemana = int(diaSemana)

if diaSemana == 1:
  print("Domingo")
elif diaSemana == 2:
  print("Segunda-feira")
elif diaSemana == 3:
  print("Terça-feira")
elif diaSemana == 4:
  print("Quarta-feira")
elif diaSemana == 5:
  print("Quinta-feira")
elif diaSemana == 6:
  print("Sexta-feira")
elif diaSemana == 7:
  print("Sabado")
