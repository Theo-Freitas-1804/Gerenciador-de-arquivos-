from login_ADMIN import salvar_senha_hash

senha = input("Crie sua senha , administrador")
salvar_senha_hash(senha)
print("Senha estabelecida com sucesso")
