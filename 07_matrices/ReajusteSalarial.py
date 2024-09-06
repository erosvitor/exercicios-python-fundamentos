#!python3

"""
  Criar um programa que armazene os dados dos funcionários em uma matriz e depois aplique o reajuste
  salarial e mostre na tela os salários reajustados.

    Dados dos funcionários

      1001,1,5400.00
      1002,1,5500.00
      1003,2,4250.00
      1004,2,4400.00
      1005,2,4180.00
      1006,3,2700.00

      onde:

        - A primeira coluna é o código do funcionário
        - A segunda coluna é o código do cargo do funcionário
        - A terceira coluna é o salário do funcionário

    Regras para o reajuste salarial

      - Para cargos de gerêntes (código 1) reajustar em 10%
      - Para cargos de supervisores (código 2) reajustar em 8%
      - Para cargos de analistas (código 3) reajustar em 6%
"""

print("Reajuste Salarial")
print("")

dadosFuncionarios = [
  [1001,1,5400.00],
  [1002,1,5500.00],
  [1003,2,4250.00],
  [1004,2,4400.00],
  [1005,2,4180.00],
  [1006,3,2700.00]
]

for func in dadosFuncionarios:
  if func[1] == 1:
    func[2] += func[2] * 0.10
  elif func[1] == 2:
    func[2] += func[2] * 0.08
  elif func[1] == 3:
    func[2] += func[2] * 0.06

for func in dadosFuncionarios:
  print(f"Código funcionário: {func[0]}, salário reajustado: {func[2]}")
