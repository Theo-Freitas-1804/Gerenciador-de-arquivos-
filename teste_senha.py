from login_ADMIN import salvar_senha_hash , autenticar

senha = input("Digite sua senha")

if autenticar(senha):
    print("✔️ Acesso autorizado , bem-vindo , administrador")
else:
    print ("Senha incorreta , acesso bloqueado")
