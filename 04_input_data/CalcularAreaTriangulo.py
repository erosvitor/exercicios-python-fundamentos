#!python3

"""
  Escreva um programa para calcular a área de um triângulo. O programa deve solicitar ao usuário a
  base e a altura do triângulo. Deve calcular a área e depois mostrar o resultado na tela. A fórmula
  para calcular a área de um triângulo é A = (base x altura) / 2.
"""

print("Calcular área de um triângulo")
print("")

base = input("Digite a base do triângulo: ")
altura = input("Digite a altura do triângulo: ")

area = (int(base) * int(altura)) / 2
print(f"A área do triângulo é: {area}")

