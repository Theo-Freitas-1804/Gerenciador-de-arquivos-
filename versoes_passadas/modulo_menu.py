import os
import json
from modulo_funcoes import *
from modulo_log_geral import registrar_log_geral, exibir_log
from modulo_log import registrar_log_lixeira
from config_V2 import caminhos_padrao, extensoes, PASTA_LOGS

# Inicialização do log da lixeira
caminho_log_lixeira = os.path.join(PASTA_LOGS, "log_lixeira.json")
if os.path.exists(caminho_log_lixeira):
    with open(caminho_log_lixeira, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
else:
    dados = {"logs": []}

# Saudação inicial
def saudacao():
    print("Olá, bem-vindo ao seu gerenciador de arquivos | Organize tudo com poucos cliques")

# Funções de menu
def sair():
    print("Saindo do programa. Até logo!")
    exit()

def opcao_categorizar_arquivos(caminho_partida):
    categorizar_arquivos(caminho_partida)
    registrar_log_geral(
        acao="Categorizar Arquivos",
        arquivo="Vários Arquivos",
        origem=caminho_partida,
        destino="Pastas de categorias"
    )
    print("\nArquivos categorizados com sucesso!")

def opcao_criar_arquivos(caminho_partida):
    nome = input("Nome do arquivo: ")
    extensao = input("Extensão do arquivo (ex: .txt): ")
    caminho_escolhido = input("Caminho onde criar (pressione Enter para usar o caminho inicial): ")
    caminho_final = caminho_partida if not caminho_escolhido.strip() else caminho_escolhido
    quantidade = int(input("Quantidade de arquivos: "))

    criar_arquivos_em_branco(nome, extensao, caminho_final, quantidade)
    registrar_log_geral(
        acao="Criar Arquivos",
        arquivo="Vários arquivos",
        origem=None,
        destino=caminho_final
    )
    print("Arquivos criados com sucesso!")

def opcao_mover_arquivos():
    nome = input("Nome do arquivo: ")
    origem = input("Pasta antiga: ")
    destino = input("Pasta nova: ")

    mover_arquivos(nome, origem, destino)
    registrar_log_geral(
        acao="Mover Arquivo",
        arquivo=nome,
        origem=origem,
        destino=destino
    )
    print("Arquivo movido com sucesso.")

def opcao_exibir_arquivos(caminho_partida):
    exibir_arquivos(caminho_partida)
    registrar_log_geral(
        acao="Exibir Arquivos",
        arquivo=None,
        origem=caminho_partida,
        destino=""
    )
    print("Arquivos exibidos com sucesso.")

def opcao_lixeira():
    manusear_lixeira()
    registrar_log_lixeira(
        acao="Manusear Lixeira",
        arquivo="arquivo(s) da lixeira",
        origem="lixeira",
        destino="ação aplicada"
    )
    print("Lixeira manipulada com sucesso.")

def opcao_renomear_arquivos():
    pasta = input("Digite o caminho da pasta onde quer renomear os arquivos: ")
    novo_nome = input("Digite o novo nome: ")

    renomear_arquivos(pasta, novo_nome)
    registrar_log_geral(
        acao="Renomear Arquivos",
        arquivo="Vários arquivos",
        origem=pasta,
        destino=f"{pasta} (renomeado para {novo_nome})"
    )
    print("Arquivos renomeados com sucesso.")

def opcao_copiar_arquivos():
    nome = input("Nome do arquivo: ")
    origem = input("Caminho de origem: ")
    destino = input("Caminho de destino: ")

    copiar_arquivo(nome, origem, destino)
    registrar_log_geral(
        acao="Copiar Arquivo",
        arquivo=nome,
        origem=origem,
        destino=destino
    )
    print("Arquivo copiado com sucesso.")

# Menu principal
def menu():
    saudacao()
    caminho_partida = input("\nDigite um caminho inicial: ")
    
    opcoes = {
        "1": lambda: opcao_categorizar_arquivos(caminho_partida),
        "2": lambda: opcao_criar_arquivos(caminho_partida),
        "3": opcao_mover_arquivos,
        "4": lambda: opcao_exibir_arquivos(caminho_partida),
        "5": opcao_lixeira,
        "6": opcao_renomear_arquivos,
        "7": opcao_copiar_arquivos,
        "8": lambda: exibir_log(os.path.join(PASTA_LOGS, "log_geral.json")),
        "9": sair
    }

    while True:
        print("\n--- MENU ---")
        print("1. Categorizar Arquivos")
        print("2. Criar Arquivos")
        print("3. Mover Arquivos")
        print("4. Exibir Arquivos")
        print("5. Lixeira")
        print("6. Renomear Arquivos")
        print("7. Copiar Arquivos")
        print("8. Exibir Log")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")
        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("Opção inválida. Tente novamente.")

# Execução do menu
if __name__ == "__main__":
    menu()