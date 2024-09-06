#!python3

"""
  Criar um programa que solicite um login e verifique se o login é válido. O login será válido ser for
  diferente de branco. Exibir a mensagem 'Login Válido' caso o login seja diferente de branco, caso
  contrário, exibir a mensagem 'Login inválido'.
"""

print("Login")
print("")

loginValido = False

while not loginValido:
  login = input("Digite o login: ")
  if login.strip():
    print("Login válido.")
    loginValido = True
  else:
    print("Login inválido, tente novamente.")
    loginValido = False
