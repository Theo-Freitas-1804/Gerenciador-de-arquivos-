import os 
import hashlib
import json

CAMINHO_SEGURANCA = "dados/seguranca.json"
def gerar_hash(senha: str ) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()

def salvar_senha_hash(senha):
    hash_senha = gerar_hash(senha)
    os.makedirs("dados" , exist_ok =True)
    with open(CAMINHO_SEGURANCA , "w") as f:
        json.dump({"senha_hash": hash_senha} , f)

def autenticar(senha_digitada: str) -> bool:
    if not os.path.exists(CAMINHO_SEGURANCA):
        print("A senha admin ainda não foi definida")
        return False
    with open(CAMINHO_SEGURANCA , "r") as f:
        dados = json.load(f)
    hash_armazenado = dados.get("senha_hash")
    return gerar_hash(senha_digitada) == hash_armazenado
