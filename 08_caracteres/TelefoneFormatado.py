#!python3

"""
  Criar um programa que solicite ao usuário um número de telefone e depois mostre na tela o número
  formatado seguindo a mascara de formatação (XX) XXXXX-XXXX. Obs.: Independente do jeito que o usuário
  informe o número do telefone, o programa sempre deverá mostrar o telefone seguindo o formato
  (XX) XXXXX-XXXX.
"""

print("Número Telefone Formatado")
print()
    
telefone = input("Digite um número de telefone: ")

telefoneSemFormatacao = ""
for i in range(0, len(telefone)):
  caractere = telefone[i]
  if caractere.isdigit():
    telefoneSemFormatacao += caractere
    
telefoneComFormatacao = ""
telefoneComFormatacao += "("
telefoneComFormatacao += telefoneSemFormatacao[0:2]
telefoneComFormatacao += ")"
    
telefoneComFormatacao += " "
    
telefoneComFormatacao += telefoneSemFormatacao[2:7]
telefoneComFormatacao += "-"
telefoneComFormatacao += telefoneSemFormatacao[7:11]

print(telefoneComFormatacao)
